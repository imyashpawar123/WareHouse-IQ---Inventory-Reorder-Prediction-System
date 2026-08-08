// Sales Trend Chart

const salesCanvas = document.getElementById("salesChart");

if (salesCanvas) {

    new Chart(salesCanvas, {
        type: "line",
        data: {
            labels: monthLabels,
            datasets: [{
                label: "Sales",
                data: monthValues,
                borderWidth: 3,
                tension: 0.4,
                fill: false
            }]
        }
    });

}

// Category Chart
// Stock Status Chart

const stockCanvas = document.getElementById("stockChart");

if (stockCanvas) {

    new Chart(stockCanvas, {

        type: "doughnut",

        data: {

            labels: stockLabels,

            datasets: [{

                label: "Stock Status",

                data: stockValues

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    position: "top"

                }

            }

        }

    });

}