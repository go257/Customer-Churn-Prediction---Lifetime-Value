def calculate_ltv(tenure, monthly_charges):

    return round(
        tenure * monthly_charges,
        2
    )


def predict_customer(tenure, monthly_charges):

    if tenure < 12 and monthly_charges > 70:

        return "Customer likely to churn"

    return "Customer will stay"


def customer_analysis(tenure, monthly_charges):

    prediction = predict_customer(
        tenure,
        monthly_charges
    )

    ltv = calculate_ltv(
        tenure,
        monthly_charges
    )

    return prediction, ltv


if __name__ == "__main__":

    tenure = 20
    monthly_charges = 80

    prediction, ltv = customer_analysis(
        tenure,
        monthly_charges
    )

    print("Customer Prediction:", prediction)
    print("Customer LTV:", ltv)