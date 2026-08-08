from flask import Flask, render_template, request, redirect, url_for, session, send_file
import pandas as pd
import joblib
import numpy as np
from math import ceil
from flask import send_file
app = Flask(__name__)
app.secret_key = "warehouseiq_secret"

# Load ML model
model = joblib.load("models/reorder_model.pkl")
scaler = joblib.load("models/scaler.pkl")

USERNAME = "admin"
PASSWORD = "Admin@123"


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:

            session["user"] = username
            return redirect(url_for("dashboard"))

        else:
            message = "Invalid Username or Password"

    return render_template("login.html", message=message)


def check_login():

    if "user" not in session:
        return False
    return True

# Create Stock Status Dynamically

def get_status(stock):

    if stock < 50:
        return "Critical"

    elif stock < 100:
        return "Low"

    elif stock < 200:
        return "Medium"

    else:
        return "Normal"

    
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    df = pd.read_csv("dataset/inventory_clean.csv")


    df["Status"] = df["Inventory Level"].apply(get_status)
    total_products = df["Product ID"].nunique()

    low_stock = len(df[df["Inventory Level"] < 50])

    stores = df["Store ID"].nunique()

    average_sales = int(df["Units Sold"].mean())

    revenue = int((df["Units Sold"] * df["Price"]).sum())

    forecast = int(df["Demand Forecast"].mean())
    # Category-wise Products
    category_labels = df["Category"].value_counts().index.tolist()
    category_values = df["Category"].value_counts().values.tolist()
    # Stock Status Count
    stock_status = df["Status"].value_counts()

    stock_labels = stock_status.index.tolist()
    stock_values = stock_status.values.tolist()
    # Monthly Sales
    monthly_sales = df.groupby("Month")["Units Sold"].sum()

    month_labels = monthly_sales.index.astype(str).tolist()
    month_values = monthly_sales.values.tolist()

    

    return render_template(
    "dashboard.html",

    total_products=total_products,
    low_stock=low_stock,

    total_stores=stores,
    total_revenue=revenue,

    average_sales=average_sales,
    forecast=forecast,

    category_labels=category_labels,
    category_values=category_values,

    month_labels=month_labels,
    month_values=month_values,

    stock_labels=stock_labels,
    stock_values=stock_values
)

   
@app.route("/inventory")
def inventory():

    if "user" not in session:
        return redirect(url_for("login"))

    df = pd.read_csv("dataset/inventory.csv")

    # Search and Filters
    search = request.args.get("search", "").strip()
    category = request.args.get("category", "")
    region = request.args.get("region", "")

    if search:
        df = df[
            df.astype(str)
            .apply(lambda x: x.str.contains(search, case=False, na=False))
            .any(axis=1)
        ]

    if category:
        df = df[df["Category"] == category]

    if region:
        df = df[df["Region"] == region]


    def get_status(stock):
        if stock >= 100:
            return "Normal"
        elif stock >= 50:
            return "Medium"
        elif stock >= 20:
            return "Low"
        else:
            return "Critical"


    df["Status"] = df["Inventory Level"].apply(get_status)


    total_products = df["Product ID"].nunique()
    total_stores = df["Store ID"].nunique()
    low_stock = len(df[df["Inventory Level"] < 50])
    critical_stock = len(df[df["Inventory Level"] < 20])
    total_categories = df["Category"].nunique()

    # Pagination
    page = request.args.get("page", 1, type=int)
    per_page = 20

    total_records = len(df)
    total_pages = ceil(total_records / per_page)

    start = (page - 1) * per_page
    end = start + per_page

    inventory_data = df.iloc[start:end]
    # Pagination window
    start_page = max(1, page - 2)
    end_page = min(total_pages, page + 2)

    categories = sorted(df["Category"].unique().tolist())
    regions = sorted(df["Region"].unique().tolist())

    return render_template(
    "inventory.html",
    inventory=inventory_data.to_dict(orient="records"),

    total_products=total_products,
    total_stores=total_stores,
    low_stock=low_stock,
    critical_stock=critical_stock,
    total_categories=total_categories,
    page=page,
    total_pages=total_pages,

    # Pagination
    start_page=start_page,
    end_page=end_page,

    # Filters
    search=search,
    category=category,
    region=region,
)

@app.route("/analytics")
def analytics():

    if "user" not in session:
        return redirect(url_for("login"))

    df = pd.read_csv("dataset/inventory.csv")

    # ==========================
    # KPI Cards
    # ==========================

    total_sales = int(df["Units Sold"].sum())

    total_revenue = round(
        (df["Units Sold"] * df["Price"]).sum(), 2
    )

    avg_inventory = round(
        df["Inventory Level"].mean()
    )

    reorder_items = len(
        df[df["Inventory Level"] < 50]
    )

    # ==========================
    # Analytics Page
    # Charts are generated separately
    # using analytics_charts.py
    # ==========================

    return render_template(
        "analytics.html",

        total_sales=total_sales,
        total_revenue=total_revenue,
        avg_inventory=avg_inventory,
        reorder_items=reorder_items
    )

@app.route("/reports")
def reports():

    if "user" not in session:
        return redirect(url_for("login"))

    df = pd.read_csv("dataset/inventory_clean.csv")

    total_reports = len(df)
    low_stock = len(df[df["Inventory Level"] < 50])
    revenue = int((df["Units Sold"] * df["Price"]).sum())
    avg_inventory = int(df["Inventory Level"].mean())

    inventory = df.to_dict(orient="records")
    recent_reports = [

    {
        "name": "Inventory Summary",
        "date": "04 Aug 2026",
        "format": "CSV",
        "status": "Ready",
        "route": "inventory_summary_report"
    },

    {
        "name": "Sales Report",
        "date": "04 Aug 2026",
        "format": "CSV",
        "status": "Ready",
        "route": "sales_report"
    },

    {
        "name": "Low Stock Report",
        "date": "04 Aug 2026",
        "format": "CSV",
        "status": "Ready",
        "route": "low_stock_report"
    },

    {
        "name": "Revenue Report",
        "date": "04 Aug 2026",
        "format": "CSV",
        "status": "Ready",
        "route": "revenue_report"
    }

]
    return render_template(
        "reports.html",

        total_reports=total_reports,
        low_stock=low_stock,
        revenue=revenue,
        avg_inventory=avg_inventory,

        inventory=inventory,
        recent_reports=recent_reports
    )

from flask import send_file
import os

@app.route("/export_csv")
def export_csv():

    if "user" not in session:
        return redirect(url_for("login"))

    file_path = "dataset/inventory_clean.csv"

    return send_file(
        file_path,
        as_attachment=True,
        download_name="WarehouseIQ_Report.csv",
        mimetype="text/csv"
    )

from flask import Response

@app.route("/inventory_summary_report")
def inventory_summary_report():

    if "user" not in session:
        return redirect(url_for("login"))

    df = pd.read_csv("dataset/inventory_clean.csv")

    # Inventory Summary Columns
    report = df[
        [
            "Store ID",
            "Product ID",
            "Category",
            "Inventory Level",
            "Units Sold",
            "Demand Forecast"
        ]
    ]

    return Response(
        report.to_csv(index=False),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=Inventory_Summary_Report.csv"
        }
    )

@app.route("/sales_report")
def sales_report():

    if "user" not in session:
        return redirect(url_for("login"))

    df = pd.read_csv("dataset/inventory_clean.csv")

    report = df[
        [
            "Date",
            "Store ID",
            "Product ID",
            "Category",
            "Units Sold",
            "Price"
        ]
    ]

    return Response(
        report.to_csv(index=False),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=Sales_Report.csv"
        }
    )

@app.route("/low_stock_report")
def low_stock_report():

    if "user" not in session:
        return redirect(url_for("login"))

    df = pd.read_csv("dataset/inventory_clean.csv")

    report = df[df["Inventory Level"] < 50]

    return Response(
        report.to_csv(index=False),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=Low_Stock_Report.csv"
        }
    )

@app.route("/revenue_report")
def revenue_report():

    if "user" not in session:
        return redirect(url_for("login"))

    df = pd.read_csv("dataset/inventory_clean.csv")

    df["Revenue"] = df["Units Sold"] * df["Price"]

    report = df[
        [
            "Store ID",
            "Product ID",
            "Category",
            "Units Sold",
            "Price",
            "Revenue"
        ]
    ]

    return Response(
        report.to_csv(index=False),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=Revenue_Report.csv"
        }
    )

@app.route("/prediction", methods=["GET", "POST"])
def prediction():

    if not check_login():
        return redirect(url_for("login"))

    prediction = None
    confidence = None

    # Default values (GET request साठी)
    inventory = ""
    sold = ""
    demand = ""
    price = ""
    discount = ""
    competitor = ""
    weather = 0
    holiday = 0
    season = 0

    if request.method == "POST":

        inventory = float(request.form["inventory"])
        sold = float(request.form["sold"])
        demand = float(request.form["demand"])
        price = float(request.form["price"])
        discount = float(request.form["discount"])
        competitor = float(request.form["competitor"])

        weather = int(request.form["weather"])
        holiday = int(request.form["holiday"])
        season = int(request.form["season"])

        data = np.array([[
            inventory,
            sold,
            demand,
            price,
            discount,
            competitor,
            weather,
            holiday,
            season
        ]])

        data = scaler.transform(data)

        result = model.predict(data)[0]
        probability = model.predict_proba(data)[0]

        confidence = round(max(probability) * 100, 2)

        if result == 1:
            prediction = "Reorder Required"
        else:
            prediction = "No Reorder Required"

    return render_template(
        "prediction.html",
        prediction=prediction,
        confidence=confidence,
        inventory=inventory,
        sold=sold,
        demand=demand,
        price=price,
        discount=discount,
        competitor=competitor,
        weather=weather,
        holiday=holiday,
        season=season
    )


@app.route("/download-report")
def download_report():

    if not check_login():
        return redirect(url_for("login"))

    return send_file(
        "dataset/inventory.csv",
        as_attachment=True,
        download_name="Warehouse_Report.csv"
    )

@app.route("/logout")
def logout():

    session.clear()
    return redirect(url_for("login"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)