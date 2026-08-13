document.addEventListener("DOMContentLoaded", function () {

    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        const target = parseFloat(
            counter.getAttribute("data-target")
        ) || 0;

        let current = 0;

        const duration = 1200;
        const steps = 60;
        const increment = target / steps;

        const timer = setInterval(() => {

            current += increment;

            if (current >= target) {
                current = target;
                clearInterval(timer);
            }

            // Decimal value
            if (target % 1 !== 0) {
                counter.innerText = current.toFixed(2);
            }

            // Integer value
            else {
                counter.innerText = Math.floor(current);
            }

        }, duration / steps);

    });

});