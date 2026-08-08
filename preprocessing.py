import pandas as pd
from sklearn.preprocessing import LabelEncoder

print("Loading Dataset...")

df = pd.read_csv("dataset/inventory.csv")

print("Cleaning Dataset...")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
for column in df.columns:
    if pd.api.types.is_numeric_dtype(df[column]):
        df[column] = df[column].fillna(df[column].median())
    else:
        df[column] = df[column].fillna(df[column].mode()[0])

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# Create Month and Year
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

# Encode categorical columns
encoder = LabelEncoder()

categorical_columns = [
    "Category",
    "Region",
    "Weather Condition",
    "Holiday/Promotion",
    "Seasonality"
]

for column in categorical_columns:
    df[column] = encoder.fit_transform(df[column])

# Create Reorder column
df["Reorder"] = (
    df["Inventory Level"] < df["Demand Forecast"]
).astype(int)

# Save cleaned dataset
df.to_csv("dataset/inventory_clean.csv", index=False)

print("===================================")
print("Preprocessing Completed Successfully")
print("Rows :", len(df))
print("Columns :", len(df.columns))
print("Saved : dataset/inventory_clean.csv")
print("===================================")