import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("../prediction_history.csv")

# Create figure
plt.figure(figsize=(14, 10))

# -------------------------
# 1. Bar Chart
# -------------------------

plt.subplot(2, 2, 1)

prediction_counts = data["Prediction"].value_counts()

plt.bar(
    prediction_counts.index,
    prediction_counts.values
)

plt.title("Prediction Count")
plt.xlabel("Prediction")
plt.ylabel("Count")

plt.xticks(rotation=20)


# -------------------------
# 2. Pie Chart
# -------------------------

plt.subplot(2, 2, 2)

plt.pie(
    prediction_counts.values,
    labels=prediction_counts.index,
    autopct="%1.1f%%"
)

plt.title("Prediction Distribution")


# -------------------------
# 3. Line Chart
# -------------------------

plt.subplot(2, 1, 2)

data = data.sort_values("Tenure")

plt.plot(
    data["Tenure"],
    data["monthly_charges"],
    marker="o"
)

plt.title("Tenure vs Monthly Charges")
plt.xlabel("Tenure")
plt.ylabel("Monthly Charges")

plt.grid(True)


# -------------------------
# Show Dashboard
# -------------------------

plt.suptitle(
    "Customer Churn Prediction Dashboard",
    fontsize=16
)

plt.tight_layout()

plt.show()