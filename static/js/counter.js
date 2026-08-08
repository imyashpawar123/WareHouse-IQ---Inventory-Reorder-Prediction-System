document.addEventListener("DOMContentLoaded", () => {

    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        const target = parseFloat(counter.dataset.target);
        const duration = 2000; // 2 seconds (increase for slower animation)
        const startTime = performance.now();

        function animate(currentTime) {

            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);

            // Ease-Out Animation
            const easeOut = 1 - Math.pow(1 - progress, 3);

            const value = target * easeOut;

            if (Number.isInteger(target)) {
                counter.innerText = Math.floor(value).toLocaleString();
            } else {
                counter.innerText = value.toLocaleString(undefined, {
                    minimumFractionDigits: 2,
                    maximumFractionDigits: 2
                });
            }

            if (progress < 1) {
                requestAnimationFrame(animate);
            } else {
                if (Number.isInteger(target)) {
                    counter.innerText = target.toLocaleString();
                } else {
                    counter.innerText = target.toLocaleString(undefined, {
                        minimumFractionDigits: 2,
                        maximumFractionDigits: 2
                    });
                }
            }
        }

        requestAnimationFrame(animate);

    });

});