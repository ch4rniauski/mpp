initWebSocketUi();

function initWebSocketUi() {
    const statusEl = document.getElementById("connection-status");
    const connectBtn = document.getElementById("connect-btn");
    const disconnectBtn = document.getElementById("disconnect-btn");
    const logEl = document.getElementById("log");

    const popup = document.getElementById("assistant-popup");
    const popupText = document.getElementById("popup-text");
    const popupClose = document.getElementById("popup-close");

    let socket = null;

    function setStatus(state, text) {
        statusEl.textContent = text;

        statusEl.classList.remove(
            "status--connected",
            "status--disconnected",
            "status--connecting"
        );

        if (state === "connected") {
            statusEl.classList.add("status--connected");
        } else if (state === "connecting") {
            statusEl.classList.add("status--connecting");
        } else {
            statusEl.classList.add("status--disconnected");
        }
    }

    function addLog(message) {
        const li = document.createElement("li");
        const timeSpan = document.createElement("span");
        timeSpan.className = "log__time";
        timeSpan.textContent = new Date().toLocaleTimeString();

        const textSpan = document.createElement("span");
        textSpan.textContent = message;

        li.appendChild(timeSpan);
        li.appendChild(textSpan);
        logEl.appendChild(li);
        logEl.scrollTop = logEl.scrollHeight;
    }

    function showPopup(message) {
        popupText.textContent = message;
        popup.style.display = "block";
    }

    function hidePopup() {
        popup.style.display = "none";
    }

    popupClose.addEventListener("click", hidePopup);

    function connect() {
        if (socket && (socket.readyState === WebSocket.OPEN || socket.readyState === WebSocket.CONNECTING)) {
            return;
        }

        const url = "ws://localhost:5267/ws";

        addLog(`Подключение к ${url}...`);
        setStatus("connecting", "Подключение...");

        socket = new WebSocket(url);

        socket.onopen = () => {
            setStatus("connected", "Подключено");
            connectBtn.disabled = true;
            disconnectBtn.disabled = false;
            addLog("Соединение открыто");
        };

        socket.onmessage = (event) => {
            const text = event.data;
            addLog(`Сообщение: ${text}`);
            showPopup(text);
        };

        socket.onerror = (event) => {
            console.error("WebSocket error", event);
            addLog("Ошибка WebSocket (подробности в консоли)");
        };

        socket.onclose = (event) => {
            addLog(
                `Соединение закрыто (code=${event.code}, reason=${event.reason || "нет"})`
            );
            setStatus("disconnected", "Отключено");
            connectBtn.disabled = false;
            disconnectBtn.disabled = true;
        };
    }

    function disconnect() {
        if (!socket) {
            return;
        }
        addLog("Закрываем соединение по инициативе клиента");
        socket.close(1000, "Client disconnect");
        socket = null;
    }

    connectBtn.addEventListener("click", connect);
    disconnectBtn.addEventListener("click", disconnect);
}
