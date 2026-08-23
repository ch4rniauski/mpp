const API_BASE_URL = "http://localhost:5002/api/credits";

async function loadCredits() {
    const res = await fetch(API_BASE_URL);
    const data = await res.json();

    const container = document.getElementById('credits');
    container.innerHTML = '';

    data.forEach(c => {
        const div = document.createElement('div');
        div.className = 'credit-item';

        div.innerHTML = `
            <div><span>Name:</span> ${c.name}</div>
            <div><span>Amount:</span> ${c.amount}</div>
            <div><span>Rate:</span> ${c.interestRate}%</div>
            <div><span>Issue Date:</span> ${c.issueDate.substring(0,10)}</div>
            <div><span>Term:</span> ${c.termMonths} months</div>
            <button onclick="deleteCredit(${c.id})">Delete</button>
            <button onclick="showUpdateForm(${c.id}, '${c.name}', ${c.amount}, ${c.interestRate}, '${c.issueDate}', ${c.termMonths})">Update</button>
        `;

        container.appendChild(div);
    });
}

async function addCredit() {
    const credit = {
        name: document.getElementById('name').value,
        amount: parseFloat(document.getElementById('amount').value),
        interestRate: parseFloat(document.getElementById('rate').value),
        issueDate: document.getElementById('date').value,
        termMonths: parseInt(document.getElementById('term').value)
    };

    await fetch(API_BASE_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credit)
    });

    loadCredits();
}

async function deleteCredit(id) {
    await fetch(`${API_BASE_URL}/${id}`, { method: 'DELETE' });
    loadCredits();
}

function showUpdateForm(id, name, amount, rate, date, term) {
    const container = document.getElementById('credits');

    const form = document.createElement('div');
    form.className = 'update-form';

    form.innerHTML = `
        <h3>Update Credit #${id}</h3>
        <input id="u_name" value="${name}"><br>
        <input id="u_amount" type="number" value="${amount}"><br>
        <input id="u_rate" type="number" step="0.01" value="${rate}"><br>
        <input id="u_date" type="date" value="${date.substring(0,10)}"><br>
        <input id="u_term" type="number" value="${term}"><br>
        <button onclick="updateCredit(${id})">Save</button>
    `;

    container.prepend(form);
}

async function updateCredit(id) {
    const credit = {
        id: id,
        name: document.getElementById('u_name').value,
        amount: parseFloat(document.getElementById('u_amount').value),
        interestRate: parseFloat(document.getElementById('u_rate').value),
        issueDate: document.getElementById('u_date').value,
        termMonths: parseInt(document.getElementById('u_term').value)
    };

    await fetch(`${API_BASE_URL}/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credit)
    });

    loadCredits();
}
