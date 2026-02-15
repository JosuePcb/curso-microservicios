document.addEventListener('DOMContentLoaded', () => {
    fetchData();
});

async function fetchData() {
    try {
        const response = await fetch('data.json');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        populateDashboard(data);
    } catch (error) {
        console.error('Fetch error:', error);
    }
}

function populateDashboard(data) {
    // Populate metrics cards
    const metricsContainer = document.querySelector('.metrics-cards');
    if (data.metrics && metricsContainer) {
        data.metrics.forEach(metric => {
            const card = document.createElement('div');
            card.className = 'card';
            card.innerHTML = `<h3>${metric.title}</h3><p>${metric.value}</p>`;
            metricsContainer.appendChild(card);
        });
    }

    // Populate data table
    const tableBody = document.querySelector('.data-table tbody');
    if (data.transactions && tableBody) {
        data.transactions.forEach(tx => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${tx.id}</td>
                <td>${tx.product}</td>
                <td>${tx.date}</td>
                <td>$${tx.amount.toFixed(2)}</td>
            `;
            tableBody.appendChild(row);
        });
    }
}
