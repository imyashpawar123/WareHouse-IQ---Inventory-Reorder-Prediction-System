import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("dataset/inventory.csv")

print("Dataset loaded successfully!")


# ==========================
# Images Folder
# ==========================

output_dir = "static/images"

os.makedirs(output_dir, exist_ok=True)


# ==========================================================
# 1. INVENTORY BY CATEGORY - BAR CHART
# ==========================================================

category = (
    df.groupby("Category")["Inventory Level"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

category.plot(kind="bar")

plt.title("Inventory by Category")
plt.xlabel("Category")
plt.ylabel("Total Inventory Level")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "category_inventory.png"),
    dpi=150
)

plt.close()

print("✓ Category bar chart saved")


# ==========================================================
# 2. INVENTORY BY REGION - PIE CHART
# ==========================================================

region = (
    df.groupby("Region")["Inventory Level"]
    .sum()
)

plt.figure(figsize=(8, 8))

plt.pie(
    region.values,
    labels=region.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Inventory Distribution by Region")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "region_inventory_pie.png"),
    dpi=150
)

plt.close()

print("✓ Region pie chart saved")


# ==========================================================
# 3. MONTHLY SALES - LINE CHART
# ==========================================================

df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = (
    df.groupby(df["Date"].dt.month)["Units Sold"]
    .sum()
)

month_names = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
]

monthly_sales.index = [
    month_names[i - 1]
    for i in monthly_sales.index
]

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Units Sold")

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "monthly_sales.png"),
    dpi=150
)

plt.close()

print("✓ Monthly sales line chart saved")


# ==========================================================
# 4. SALES vs REVENUE - BAR + LINE CHART
# ==========================================================

monthly_data = df.groupby(
    df["Date"].dt.month
).agg(
    sales=("Units Sold", "sum"),
    revenue=("Price", lambda x: 0)
).reset_index()

# Calculate actual revenue
df["Revenue"] = df["Units Sold"] * df["Price"]

monthly_revenue = (
    df.groupby(df["Date"].dt.month)["Revenue"]
    .sum()
)

monthly_sales_2 = (
    df.groupby(df["Date"].dt.month)["Units Sold"]
    .sum()
)

months = [
    month_names[i - 1]
    for i in monthly_sales_2.index
]


fig, ax1 = plt.subplots(figsize=(11, 6))

# Bar chart - Sales
ax1.bar(
    months,
    monthly_sales_2.values,
    alpha=0.7,
    label="Units Sold"
)

ax1.set_xlabel("Month")
ax1.set_ylabel("Units Sold")

# Line chart - Revenue
ax2 = ax1.twinx()

ax2.plot(
    months,
    monthly_revenue.values,
    marker="o",
    linewidth=2,
    label="Revenue"
)

ax2.set_ylabel("Revenue")

plt.title("Monthly Sales vs Revenue")

fig.tight_layout()

plt.savefig(
    os.path.join(output_dir, "sales_revenue_combined.png"),
    dpi=150
)

plt.close()

print("✓ Sales + Revenue combined chart saved")


# ==========================================================
# 5. CORRELATION HEATMAP
# ==========================================================

numeric_columns = [
    "Inventory Level",
    "Units Sold",
    "Units Ordered",
    "Demand Forecast",
    "Price",
    "Discount",
    "Competitor Pricing"
]

correlation = df[numeric_columns].corr()

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Inventory Dataset Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "correlation_heatmap.png"),
    dpi=150
)

plt.close()

print("✓ Correlation heatmap saved")


# ==========================================================
# 6. DISCOUNT vs UNITS SOLD - BAR CHART
# ==========================================================

discount_sales = (
    df.groupby("Discount")["Units Sold"]
    .mean()
    .sort_index()
)

plt.figure(figsize=(10, 6))

discount_sales.plot(
    kind="bar"
)

plt.title("Average Units Sold by Discount")
plt.xlabel("Discount (%)")
plt.ylabel("Average Units Sold")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "discount_sales.png"),
    dpi=150
)

plt.close()

print("✓ Discount sales bar chart saved")


# ==========================================================
# COMPLETE
# ==========================================================

print()
print("=" * 50)
print("All 6 Analytics Charts Generated Successfully!")
print("=" * 50)
print()
print("Images saved in:", output_dir)
print()
print("Generated files:")
print("1. category_inventory.png")
print("2. region_inventory_pie.png")
print("3. monthly_sales.png")
print("4. sales_revenue_combined.png")
print("5. correlation_heatmap.png")
print("6. discount_sales.png")