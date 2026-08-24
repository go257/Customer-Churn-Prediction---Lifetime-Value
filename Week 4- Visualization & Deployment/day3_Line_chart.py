import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("../prediction_history.csv")

# Sort by tenure
data = data.sort_values("Tenure")

# Line chart
plt.figure(figsize=(9, 5))

plt.plot(
    data["Tenure"],
    data["monthly_charges"],
    marker="o"
)

plt.title("Tenure vs Monthly Charges")
plt.xlabel("Tenure")
plt.ylabel("Monthly Charges")

plt.grid(True)
plt.tight_layout()

plt.show()