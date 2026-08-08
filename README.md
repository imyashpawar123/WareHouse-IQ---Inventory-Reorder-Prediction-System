# 📦 Warehouse IQ -- Inventory Intelligence & Reorder Prediction System

Warehouse IQ is a web-based **Inventory Intelligence and Reorder
Prediction System** developed using **Python, Flask, Pandas,
Scikit-learn, HTML, CSS, JavaScript and Bootstrap**.

The system helps warehouse/admin users monitor inventory, analyze sales
and stock information, generate reports, and predict whether a product
needs to be reordered using a trained Machine Learning model.

------------------------------------------------------------------------

## 📌 Project Overview

Managing inventory manually can make it difficult to identify low-stock
products, understand sales patterns, and decide when to reorder stock.

**Warehouse IQ** provides a centralized dashboard where users can:

-   Monitor inventory information
-   Track low-stock items
-   View sales and inventory analytics
-   Generate inventory-related reports
-   Predict reorder requirements using Machine Learning
-   View prediction confidence
-   Receive visual alerts and recommendations
-   Access the system through a login page

------------------------------------------------------------------------

## 🎯 Objectives

The main objectives of Warehouse IQ are:

1.  To create a centralized inventory management dashboard.
2.  To analyze inventory and sales data.
3.  To identify products with low inventory levels.
4.  To provide useful inventory KPIs.
5.  To automate reorder prediction using Machine Learning.
6.  To provide prediction confidence and recommendations.
7.  To provide report-generation functionality.
8.  To build a clean and responsive web interface.

------------------------------------------------------------------------

## 🚀 Main Features

### 1. 🔐 Login & Authentication

-   Admin login page
-   Session-based authentication
-   Protected application pages
-   Redirects unauthenticated users to the login page

------------------------------------------------------------------------

### 2. 📊 Dashboard

The dashboard provides an overview of the warehouse.

#### KPI Cards

-   **Total Products**
-   **Low Stock**
-   **Total Stores**
-   **Revenue**

#### Visualizations

-   Sales Trend
-   Stock Status

The dashboard is designed to give the administrator a quick overview of
the current inventory situation.

------------------------------------------------------------------------

### 3. 📦 Inventory Management

The Inventory page provides inventory information in a structured table.

The project uses cleaned inventory data for displaying records.

Inventory information includes fields such as:

-   Store ID
-   Product ID
-   Category
-   Region
-   Inventory Level
-   Units Sold
-   Units Ordered
-   Demand Forecast
-   Price
-   Discount
-   Weather Condition
-   Holiday/Promotion
-   Competitor Pricing
-   Seasonality

------------------------------------------------------------------------

### 4. 📈 Analytics

The Analytics page provides visual analysis of inventory and sales data.

The project includes data analysis using:

-   Pandas
-   Matplotlib
-   Chart.js

Analytics can be used to understand:

-   Sales trends
-   Inventory distribution
-   Category-level information
-   Regional performance
-   Product sales patterns

------------------------------------------------------------------------

### 5. 📄 Reports

The Reports section provides report-related functionality.

The project includes report categories such as:

-   Inventory Summary Report
-   Sales Report
-   Low Stock Report
-   Revenue Report

The Reports page also displays KPI information including:

-   Total Records
-   Low Stock
-   Average Inventory
-   Revenue

------------------------------------------------------------------------

### 6. 🤖 Machine Learning Reorder Prediction

The Prediction page is one of the main features of Warehouse IQ.

The user enters inventory and market-related information and clicks
**Predict Reorder**.

#### Prediction Inputs

-   Inventory Level
-   Units Sold
-   Demand Forecast
-   Price
-   Discount
-   Competitor Pricing
-   Weather
-   Holiday
-   Season

The backend processes the inputs using the trained ML model.

The model returns:

-   **Reorder Required**
-   **No Reorder Required**

------------------------------------------------------------------------

### 7. 🎯 Prediction Confidence

The prediction result also displays the model confidence.

The interface includes:

-   High Risk / Low Risk indicator
-   Prediction result
-   AI confidence percentage
-   Confidence visualization
-   Recommendation

Example:

> Reorder Required\
> Reorder this product immediately to avoid stock shortage.

or

> No Reorder Required\
> Inventory level is healthy. No reorder required.

------------------------------------------------------------------------

### 8. ✨ Prediction Page UI Features

The Prediction page contains several user-interface enhancements:

-   Predict Reorder button
-   Loading spinner while prediction is being processed
-   Reset button
-   Preserved form values after prediction
-   Prediction result remains visible after submission
-   Confidence animation
-   Centered SweetAlert notification
-   Prediction completion notification
-   Responsive Bootstrap layout

------------------------------------------------------------------------

## 🧠 Machine Learning Workflow

The Machine Learning workflow used in the project is:

``` text
Raw Inventory Dataset
        ↓
Data Cleaning / Preprocessing
        ↓
Feature Selection
        ↓
Train Machine Learning Model
        ↓
Save Trained Model
        ↓
Save Scaler
        ↓
Flask Application
        ↓
User Inputs
        ↓
Feature Scaling
        ↓
Model Prediction
        ↓
Prediction + Confidence
        ↓
Recommendation
```

------------------------------------------------------------------------

## 🛠️ Technologies Used

### Frontend

-   HTML5
-   CSS3
-   JavaScript
-   Bootstrap 5
-   Font Awesome
-   Chart.js
-   SweetAlert2

### Backend

-   Python
-   Flask

### Data Processing

-   Pandas
-   NumPy

### Machine Learning

-   Scikit-learn
-   Joblib / Pickle-based model and scaler files

### Development Tools

-   Visual Studio Code
-   Python Virtual Environment
-   Web Browser

------------------------------------------------------------------------

## 📁 Project Structure

A typical structure of the project is:

``` text
Warehouse IQ Inventory New/
│
├── app.py
├── requirements.txt
├── train_model.py
├── preprocessing.py
├── forecast.py
│
├── dataset/
│   └── inventory_clean.csv
│
├── models/
│   ├── model.pkl
│   └── scaler.pkl
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── inventory.html
│   ├── analytics.html
│   ├── reports.html
│   ├── prediction.html
│   └── 404.html
│
└── static/
    ├── css/
    │   ├── login.css
    │   ├── dashboard.css
    │   ├── inventory.css
    │   ├── analytics.css
    │   ├── reports.css
    │   └── prediction.css
    │
    ├── js/
    │   ├── login.js
    │   ├── dashboard.js
    │   ├── inventory.js
    │   ├── analytics.js
    │   ├── reports.js
    │   ├── prediction.js
    │   └── counter.js
    │
    ├── graphs/
    └── images/
```

> File names can vary slightly depending on the final version of the
> project.

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### Step 1 -- Clone / Copy the Project

Place the project folder on your computer.

### Step 2 -- Open the Project

Open the project folder in Visual Studio Code.

### Step 3 -- Create Virtual Environment

``` bash
python -m venv venv
```

### Step 4 -- Activate Virtual Environment

#### Windows

``` bash
venv\Scripts\activate
```

### Step 5 -- Install Dependencies

``` bash
pip install -r requirements.txt
```

If dependencies are not available in `requirements.txt`, install the
main packages:

``` bash
pip install flask pandas numpy scikit-learn joblib matplotlib chart.js
```

------------------------------------------------------------------------

## ▶️ Running the Application

Activate the virtual environment and run:

``` bash
python app.py
```

The Flask development server will start.

Open the displayed local address in your browser, for example:

``` text
http://127.0.0.1:5000/
```

------------------------------------------------------------------------

## 🔑 Application Flow

``` text
Login
  ↓
Dashboard
  ├── Inventory
  ├── Analytics
  ├── Reports
  └── Prediction
```

### Prediction Flow

``` text
Enter Input Values
       ↓
Click Predict Reorder
       ↓
Flask Receives POST Request
       ↓
Input Data Converted to Numeric Format
       ↓
Scaler Transforms Features
       ↓
ML Model Predicts Result
       ↓
Prediction Probability Calculated
       ↓
Result Displayed
       ↓
Confidence + Recommendation
```

------------------------------------------------------------------------

## 📊 Dataset

The project uses an inventory and sales dataset containing information
related to warehouse operations.

Important features include:

  Feature              Description
  -------------------- --------------------------------
  Date                 Inventory record date
  Store ID             Store identifier
  Product ID           Product identifier
  Category             Product category
  Region               Store/warehouse region
  Inventory Level      Current stock level
  Units Sold           Number of units sold
  Units Ordered        Number of units ordered
  Demand Forecast      Forecasted demand
  Price                Product price
  Discount             Applied discount
  Weather Condition    Weather information
  Holiday/Promotion    Holiday or promotion indicator
  Competitor Pricing   Competitor product price
  Seasonality          Seasonal information

------------------------------------------------------------------------

## 🧹 Data Preprocessing

The project includes data preprocessing before using the data for
analysis and prediction.

Typical preprocessing tasks include:

-   Loading the dataset
-   Cleaning data
-   Handling required numeric values
-   Encoding categorical features
-   Selecting model features
-   Scaling numerical/model input features
-   Preparing data for Machine Learning

The trained scaler is used again during prediction so that user-entered
values are transformed consistently with the training data.

------------------------------------------------------------------------

## 🤖 Prediction Model

The trained Machine Learning model is loaded by the Flask application.

The prediction pipeline uses:

``` text
User Input
    ↓
NumPy Array
    ↓
Scaler
    ↓
Trained Model
    ↓
Prediction
    ↓
Prediction Probability
```

The application interprets the model output as:

``` text
1 → Reorder Required
0 → No Reorder Required
```

The exact model algorithm depends on the final trained model stored in
the project.

------------------------------------------------------------------------

## 🖥️ User Interface

Warehouse IQ follows a modern dashboard-style interface.

The interface includes:

-   Navigation bar
-   Sidebar/menu
-   Responsive cards
-   KPI cards
-   Charts
-   Tables
-   Forms
-   Alerts
-   Prediction result cards
-   Loading indicators
-   Reset functionality

Bootstrap is used to help maintain responsive layouts across different
screen sizes.

------------------------------------------------------------------------

## 🔔 User Feedback

The application provides visual feedback for important actions.

### Prediction

After submitting the prediction form:

``` text
Predicting...
```

is displayed while the request is being processed.

After successful prediction, the application displays a SweetAlert
notification and the prediction result.

### Reset

The **Reset** button clears the prediction state and returns the
Prediction page to its initial state.

------------------------------------------------------------------------

## 🔒 Security Notes

The current project uses Flask session-based login protection.

For a production deployment, the following should be improved:

-   Store passwords securely using password hashing.
-   Store secret keys in environment variables.
-   Use HTTPS.
-   Validate all user input on the server.
-   Restrict access to sensitive files.
-   Use production-grade Flask deployment configuration.

------------------------------------------------------------------------

## 🧪 Testing

The following areas should be tested before final submission:

### Login

-   Correct username/password
-   Incorrect credentials
-   Accessing protected pages without login

### Dashboard

-   KPI values
-   Charts
-   Navigation

### Inventory

-   Records displayed correctly
-   Search/filter functionality if enabled
-   Data consistency

### Analytics

-   Charts load correctly
-   Dataset values are reflected correctly

### Reports

-   Report pages/routes work
-   KPI values are calculated correctly

### Prediction

Test both:

``` text
Low-risk input
```

and

``` text
High-risk input
```

Verify:

-   Prediction result
-   Confidence percentage
-   Recommendation
-   Loading spinner
-   Reset button
-   Form value preservation

------------------------------------------------------------------------

## 🐛 Common Issues

### 1. ModuleNotFoundError

Install the required package:

``` bash
pip install package-name
```

### 2. Model Not Found

Check that the model file exists in the expected `models` directory.

### 3. Dataset Not Found

Check that the CSV file path used in `app.py` matches the actual dataset
location.

### 4. Flask Server Not Starting

Activate the virtual environment:

``` bash
venv\Scripts\activate
```

Then:

``` bash
python app.py
```

### 5. Prediction Scaling Warning

Make sure the feature order and feature names used during prediction
match the features used when fitting the scaler/model.

------------------------------------------------------------------------

## 🔮 Future Enhancements

Possible future improvements include:

-   Real-time inventory alerts
-   Email/SMS notifications
-   Advanced demand forecasting
-   Automatic reorder quantity prediction
-   Supplier management
-   Purchase order generation
-   User roles and permissions
-   Database integration using MySQL/PostgreSQL
-   Cloud deployment
-   Advanced ML model comparison
-   Model performance dashboard
-   Inventory forecasting charts
-   Downloadable PDF reports
-   Automated scheduled reports

------------------------------------------------------------------------

## 📈 Expected Benefits

Warehouse IQ can help users:

-   Identify low-stock situations faster
-   Understand inventory trends
-   Monitor warehouse performance
-   Reduce manual analysis
-   Support data-driven reorder decisions
-   Improve inventory visibility
-   Centralize important warehouse information

------------------------------------------------------------------------

## 🎓 Project Type

**Project:** Warehouse IQ -- Inventory Intelligence & Reorder Prediction
System

**Domain:** Data Science / Machine Learning / Inventory Management

**Application Type:** Web Application

**Backend:** Flask + Python

**Frontend:** HTML + CSS + JavaScript + Bootstrap

**ML:** Scikit-learn

**Data Processing:** Pandas + NumPy

------------------------------------------------------------------------

## 👨‍💻 Author

**Yash Pawar**

Diploma in Computer Engineering

------------------------------------------------------------------------

## 📜 License

This project is developed for educational and academic purposes.

You may modify and extend the project according to your requirements.

------------------------------------------------------------------------

## ⭐ Project Summary

**Warehouse IQ** combines inventory analytics, reporting and Machine
Learning-based reorder prediction into a single web application.

The overall system provides:

``` text
Inventory Data
      ↓
Data Processing
      ↓
Analytics
      ↓
Dashboard
      ↓
Reports
      ↓
Machine Learning
      ↓
Reorder Prediction
      ↓
Confidence + Recommendation
```

**Warehouse IQ --- Turning Inventory Data into Intelligent Decisions.
📦🤖**
