// Variables globales
let dashboardData = null;
let chart = null;

// Inicialización cuando el DOM está cargado
document.addEventListener('DOMContentLoaded', () => {
    fetchData();
    
    // Event listener para el botón de actualizar
    const refreshBtn = document.getElementById('refreshBtn');
    refreshBtn.addEventListener('click', () => {
        refreshBtn.style.transform = 'rotate(360deg)';
        setTimeout(() => {
            refreshBtn.style.transform = 'rotate(0deg)';
            fetchData();
        }, 300);
    });

    // Event listeners para la navegación
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
        });
    });
});

/**
 * Obtiene los datos del archivo JSON
 */
async function fetchData() {
    try {
        const response = await fetch('data.json');
        if (!response.ok) {
            throw new Error('Error al cargar los datos');
        }
        dashboardData = await response.json();
        populateDashboard(dashboardData);
    } catch (error) {
        console.error('Error en fetch:', error);
        showError('No se pudieron cargar los datos. Intenta nuevamente.');
    }
}

/**
 * Rellena el dashboard con datos del JSON
 */
function populateDashboard(data) {
    populateMetrics(data.metrics);
    populateTable(data.transactions);
    drawBarChart(data.transactions);
}

/**
 * Rellena las tarjetas de métricas
 */
function populateMetrics(metrics) {
    const metricsContainer = document.getElementById('metricsContainer');
    metricsContainer.innerHTML = '';

    if (!metrics || metrics.length === 0) {
        metricsContainer.innerHTML = '<p>No hay métricas disponibles.</p>';
        return;
    }

    metrics.forEach((metric, index) => {
        const card = document.createElement('div');
        card.className = 'card';
        card.style.animationDelay = `${index * 0.1}s`;
        card.innerHTML = `
            <h3>${metric.title}</h3>
            <p>${metric.value}</p>
        `;
        metricsContainer.appendChild(card);
    });
}

/**
 * Rellena la tabla de transacciones
 */
function populateTable(transactions) {
    const tableBody = document.getElementById('tableBody');
    tableBody.innerHTML = '';

    if (!transactions || transactions.length === 0) {
        tableBody.innerHTML = '<tr><td colspan="4" style="text-align: center;">No hay transacciones disponibles.</td></tr>';
        return;
    }

    transactions.forEach((tx, index) => {
        const row = document.createElement('tr');
        row.style.animationDelay = `${index * 0.05}s`;
        row.innerHTML = `
            <td>${tx.id}</td>
            <td>${tx.product}</td>
            <td>${formatDate(tx.date)}</td>
            <td style="font-weight: 600; color: #FF5A1F;">$${tx.amount.toFixed(2)}</td>
        `;
        tableBody.appendChild(row);
    });
}

/**
 * Dibuja un gráfico de barras con Canvas
 */
function drawBarChart(transactions) {
    if (!transactions || transactions.length === 0) return;

    const canvas = document.getElementById('barChart');
    const ctx = canvas.getContext('2d');

    // Dimensiones
    const canvasWidth = canvas.offsetWidth || 600;
    const canvasHeight = 280;
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;

    // Calcular datos
    const products = {};
    transactions.forEach(tx => {
        products[tx.product] = (products[tx.product] || 0) + tx.amount;
    });

    const productNames = Object.keys(products);
    const amounts = Object.values(products);
    const maxAmount = Math.max(...amounts);

    // Colores
    const colors = ['#FF5A1F', '#C9C4B4', '#191716', '#E2E4DD'];
    
    // Márgenes
    const margin = { top: 20, right: 20, bottom: 40, left: 50 };
    const chartWidth = canvasWidth - margin.left - margin.right;
    const chartHeight = canvasHeight - margin.top - margin.bottom;
    const barWidth = chartWidth / productNames.length * 0.8;
    const barSpacing = chartWidth / productNames.length;

    // Limpiar canvas
    ctx.fillStyle = '#F5F4F2';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // Dibujar barras
    productNames.forEach((product, index) => {
        const value = amounts[index];
        const barHeight = (value / maxAmount) * chartHeight;
        const x = margin.left + index * barSpacing + (barSpacing - barWidth) / 2;
        const y = margin.top + chartHeight - barHeight;

        // Barra
        ctx.fillStyle = colors[index % colors.length];
        ctx.fillRect(x, y, barWidth, barHeight);

        // Valor encima de la barra
        ctx.fillStyle = '#191716';
        ctx.font = 'bold 12px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(`$${value.toFixed(0)}`, x + barWidth / 2, y - 5);

        // Etiqueta del producto
        ctx.fillStyle = '#191716';
        ctx.font = '12px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(product, x + barWidth / 2, canvasHeight - 10);
    });

    // Línea de referencia
    ctx.strokeStyle = '#D9D4C8';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(margin.left, margin.top + chartHeight);
    ctx.lineTo(canvasWidth - margin.right, margin.top + chartHeight);
    ctx.stroke();

    // Eje Y
    ctx.strokeStyle = '#D9D4C8';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(margin.left, margin.top);
    ctx.lineTo(margin.left, margin.top + chartHeight);
    ctx.stroke();
}

/**
 * Formatea una fecha
 */
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

/**
 * Muestra un mensaje de error
 */
function showError(message) {
    const main = document.querySelector('.dashboard-main');
    const errorDiv = document.createElement('div');
    errorDiv.style.cssText = `
        background-color: #FFE5D5;
        color: #C41E3A;
        padding: 15px 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        border-left: 4px solid #FF5A1F;
    `;
    errorDiv.textContent = message;
    main.insertBefore(errorDiv, main.firstChild);
    
    setTimeout(() => {
        errorDiv.remove();
    }, 5000);
}