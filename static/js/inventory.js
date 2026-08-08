// ===============================
// Warehouse IQ - Inventory Search
// ===============================

const searchInput = document.getElementById("searchInput");

if (searchInput) {

    searchInput.addEventListener("keyup", function () {

        const filter = this.value.toLowerCase();

        const rows = document.querySelectorAll("#inventoryTable tbody tr");

        rows.forEach(function (row) {

            const text = row.innerText.toLowerCase();

            if (text.includes(filter)) {

                row.style.display = "";

            } else {

                row.style.display = "none";

            }

        });

    });

}
document.querySelectorAll(".view-btn").forEach(button => {

    button.addEventListener("click", function () {

        document.getElementById("mProduct").innerText = this.dataset.product;
        document.getElementById("mStore").innerText = this.dataset.store;
        document.getElementById("mCategory").innerText = this.dataset.category;
        document.getElementById("mRegion").innerText = this.dataset.region;
        document.getElementById("mStock").innerText = this.dataset.stock;
        document.getElementById("mSold").innerText = this.dataset.sold;
        document.getElementById("mDemand").innerText = this.dataset.demand;
        document.getElementById("mPrice").innerText = "₹ " + this.dataset.price;
        document.getElementById("mStatus").innerText = this.dataset.status;

    });

});
