from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route("/")
def dashboard():

    # Load data
    data = pd.read_csv("../prediction_history.csv")

    # Prediction count
    prediction_counts = data["Prediction"].value_counts()

    # Create dashboard
    plt.figure(figsize=(12, 8))

    # Bar chart
    plt.subplot(2, 2, 1)

    plt.bar(
        prediction_counts.index,
        prediction_counts.values
    )

    plt.title("Prediction Count")
    plt.xlabel("Prediction")
    plt.ylabel("Count")

    plt.xticks(rotation=20)


    # Pie chart
    plt.subplot(2, 2, 2)

    plt.pie(
        prediction_counts.values,
        labels=prediction_counts.index,
        autopct="%1.1f%%"
    )

    plt.title("Prediction Distribution")


    # Line chart
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

    plt.suptitle(
        "Customer Churn Prediction Dashboard"
    )

    plt.tight_layout()

    # Save chart
    chart_path = "static/dashboard.png"

    plt.savefig(
        chart_path,
        bbox_inches="tight"
    )

    plt.close()

    return render_template(
        "dashboard.html"
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )