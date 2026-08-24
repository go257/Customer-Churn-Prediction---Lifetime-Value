import pandas as pd

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Data Cleaning
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()

# Feature Engineering

# Convert SeniorCitizen (0/1) to No/Yes
df["SeniorCitizen"] = df["SeniorCitizen"].map({0: "No", 1: "Yes"})

# Create Average Monthly Spend feature
df["AverageMonthlySpend"] = df["TotalCharges"] / (df["tenure"] + 1)

# Display new features
print(df[["SeniorCitizen", "AverageMonthlySpend"]].head())

# Save engineered dataset
df.to_csv("customer_churn_feature_engineered.csv", index=False)

print("Feature Engineering Completed Successfully!")