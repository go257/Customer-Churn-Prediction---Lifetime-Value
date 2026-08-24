import pandas as pd


def predict_customer(tenure, monthly_charges):

    # Simple prediction rule
    if tenure < 12 and monthly_charges > 70:

        prediction = "Customer likely to churn"

    else:

        prediction = "Customer will stay"

    return prediction


if __name__ == "__main__":

    tenure = 10
    monthly_charges = 85

    prediction = predict_customer(
        tenure,
        monthly_charges
    )

    print("Tenure:", tenure)
    print("Monthly Charges:", monthly_charges)
    print("Prediction:", prediction)