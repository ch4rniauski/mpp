using System.Net.WebSockets;
using System.Text;
using Microsoft.AspNetCore.Mvc;

namespace laba4.Controllers;

[ApiController]
public sealed class WebSocketController : ControllerBase
{
    [Route("/ws")]
    public async Task<ActionResult> Get(CancellationToken ct)
    {
        if (!HttpContext.WebSockets.IsWebSocketRequest)
        {
            return BadRequest();
        }
        
        using var webSocket = await HttpContext.WebSockets.AcceptWebSocketAsync();
        await SendAdsLoopAsync(webSocket, ct);

        return Ok();
    }

    private static async Task SendAdsLoopAsync(WebSocket webSocket, CancellationToken ct = default)
    {
        var buffer = new byte[1];

        // Начальное чтение, чтобы держать соединение и узнать, когда клиент закрывается
        var receiveTask = webSocket.ReceiveAsync(
            new ArraySegment<byte>(buffer),
            ct);

        while (!receiveTask.IsCompleted &&
               webSocket.State == WebSocketState.Open)
        {
            var message = $"Сообщение помощника: {DateTime.Now:T}";
            var bytes = Encoding.UTF8.GetBytes(message);

            await webSocket.SendAsync(
                new ArraySegment<byte>(bytes),
                WebSocketMessageType.Text,
                endOfMessage: true,
                cancellationToken: ct);

            // ждём 10 секунд до следующего сообщения
            await Task.Delay(TimeSpan.FromSeconds(10), ct);

            // если клиент закрыл соединение — выйдем
            if (receiveTask.IsCompleted)
            {
                break;
            }
        }

        if (webSocket.State is WebSocketState.Open or WebSocketState.CloseReceived)
        {
            await webSocket.CloseAsync(
                 closeStatus: WebSocketCloseStatus.NormalClosure,
                statusDescription: "Closing",
                cancellationToken: ct);
        }
    }
}
