def calculate_ltv(tenure, monthly_charges):
    """
    Simple Customer Lifetime Value calculation.
    """

    ltv = tenure * monthly_charges

    return round(ltv, 2)


if __name__ == "__main__":

    tenure = 24
    monthly_charges = 80

    ltv = calculate_ltv(
        tenure,
        monthly_charges
    )

    print("Customer Tenure:", tenure)
    print("Monthly Charges:", monthly_charges)
    print("Estimated LTV:", ltv)