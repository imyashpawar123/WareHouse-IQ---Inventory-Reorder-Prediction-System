// Inventory by Category
new Chart(document.getElementById("categoryChart"), {
    type: "bar",
    data: {
        labels: ["Electronics", "Furniture", "Clothing", "Food"],
        datasets: [{
            label: "Inventory",
            data: [420, 310, 260, 390],
            backgroundColor: [
                "#0d6efd",
                "#20c997",
                "#ffc107",
                "#dc3545"
            ]
        }]
    }
});

// Region Wise Inventory
new Chart(document.getElementById("regionChart"), {
    type: "doughnut",
    data: {
        labels: ["North", "South", "East", "West"],
        datasets: [{
            data: [30, 25, 20, 25],
            backgroundColor: [
                "#0d6efd",
                "#198754",
                "#ffc107",
                "#dc3545"
            ]
        }]
    }
});

// Monthly Sales Trend
new Chart(document.getElementById("salesChart"), {
    type: "line",
    data: {
        labels: ["Jan","Feb","Mar","Apr","May","Jun"],
        datasets: [{
            label: "Sales",
            data: [120,150,180,170,210,250],
            borderColor: "#0d6efd",
            fill: false,
            tension: 0.4
        }]
    }
});

// Revenue Analysis
new Chart(document.getElementById("revenueChart"), {
    type: "bar",
    data: {
        labels: ["Q1","Q2","Q3","Q4"],
        datasets: [{
            label: "Revenue",
            data: [50000,70000,65000,90000],
            backgroundColor: "#198754"
        }]
    }
});

document.addEventListener("DOMContentLoaded", function () {

    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        const target = parseFloat(counter.getAttribute("data-target")) || 0;

        let current = 0;

        // Animation speed
        const duration = 1200;
        const steps = 60;
        const increment = target / steps;

        const timer = setInterval(() => {

            current += increment;

            if (current >= target) {
                current = target;
                clearInterval(timer);
            }

            // Decimal values असल्यास 2 digits
            if (target % 1 !== 0) {
                counter.innerText = current.toFixed(2);
            } else {
                counter.innerText = Math.floor(current);
            }

        }, duration / steps);

    });

});