import pandas as pd
import matplotlib.pyplot as plt
import os


# --------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------

def load_data():
    # prediction_history.csv is in the main project folder
    file_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "prediction_history.csv"
    )

    file_path = os.path.abspath(file_path)

    if not os.path.exists(file_path):
        print("Error: prediction_history.csv not found.")
        print("Looking for:", file_path)
        return None

    try:
        data = pd.read_csv(file_path)

        print("Data loaded successfully!")
        print("Total records:", len(data))

        return data

    except Exception as e:
        print("Error loading data:", e)
        return None


# --------------------------------------------------
# 2. PREDICTION SUMMARY
# --------------------------------------------------

def prediction_summary(data):

    print("\n========== PREDICTION SUMMARY ==========")

    if "prediction" not in data.columns:
        print("Prediction column not found.")
        return

    print("\nPrediction counts:")

    print(data["prediction"].value_counts())

    print("\nPrediction percentages:")

    percentage = data["prediction"].value_counts(
        normalize=True
    ) * 100

    print(percentage.round(2))


# --------------------------------------------------
# 3. CALCULATE STATISTICS
# --------------------------------------------------

def calculate_statistics(data):

    print("\n========== CUSTOMER STATISTICS ==========")

    if "tenure" in data.columns:

        print("\nTenure Statistics:")
        print(data["tenure"].describe())

    if "monthly_charges" in data.columns:

        print("\nMonthly Charges Statistics:")
        print(data["monthly_charges"].describe())


# --------------------------------------------------
# 4. CREATE CHART
# --------------------------------------------------

def create_chart(data):

    print("\n========== CREATING CHART ==========")

    if "prediction" not in data.columns:
        print("Prediction column not found.")
        return

    prediction_counts = data["prediction"].value_counts()

    plt.figure(figsize=(8, 5))

    prediction_counts.plot(
        kind="bar"
    )

    plt.title("Customer Churn Prediction Summary")
    plt.xlabel("Prediction")
    plt.ylabel("Number of Customers")

    plt.xticks(rotation=0)

    plt.tight_layout()

    # Save chart inside static folder
    static_folder = os.path.join(
        os.path.dirname(__file__),
        "static"
    )

    os.makedirs(static_folder, exist_ok=True)

    chart_path = os.path.join(
        static_folder,
        "prediction_summary.png"
    )

    plt.savefig(chart_path)

    print("Chart saved successfully:")
    print(chart_path)

    plt