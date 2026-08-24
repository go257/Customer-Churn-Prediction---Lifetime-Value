import pandas as pd
import matplotlib.pyplot as plt

# Load prediction history
data = pd.read_csv("../prediction_history.csv")

# Count predictions
prediction_counts = data["Prediction"].value_counts()

# Pie chart
plt.figure(figsize=(7, 7))

plt.pie(
    prediction_counts.values,
    labels=prediction_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Customer Churn Prediction Distribution")

plt.tight_layout()

plt.show()