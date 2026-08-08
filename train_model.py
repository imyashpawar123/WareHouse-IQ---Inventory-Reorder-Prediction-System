import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

print("=" * 50)
print("Warehouse IQ - Model Training Started")
print("=" * 50)

# Load Dataset
df = pd.read_csv("dataset/inventory_clean.csv")

# Features
X = df[
    [
        "Inventory Level",
        "Units Sold",
        "Demand Forecast",
        "Price",
        "Discount",
        "Competitor Pricing",
        "Weather Condition",
        "Holiday/Promotion",
        "Seasonality"
    ]
]

# Target
y = df["Reorder"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("\nAccuracy")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

# Create models folder if needed
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/reorder_model.pkl")

# Save scaler
joblib.dump(scaler, "models/scaler.pkl")

print("\nModel Saved Successfully")
print("models/reorder_model.pkl")
print("models/scaler.pkl")