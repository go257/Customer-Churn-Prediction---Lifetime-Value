import pandas as pd
import matplotlib.pyplot as plt

# Load prediction history
data = pd.read_csv("../prediction_history.csv")

# Count predictions
prediction_counts = data["Prediction"].value_counts()

# Bar chart
plt.figure(figsize=(8, 5))

prediction_counts.plot(
    kind="bar"
)

plt.title("Customer Churn Prediction History")
plt.xlabel("Prediction")
plt.ylabel("Count")

plt.xticks(rotation=0)
plt.tight_layout()

plt.show()