import csv
import os


FILE_NAME = "prediction_history.csv"


def save_prediction(
    tenure,
    monthly_charges,
    prediction
):

    file_exists = os.path.exists(FILE_NAME)

    with open(
        FILE_NAME,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Tenure",
                "monthly_charges",
                "Prediction"
            ])

        writer.writerow([
            tenure,
            monthly_charges,
            prediction
        ])

    print("Prediction saved successfully!")


if __name__ == "__main__":

    tenure = 20
    monthly_charges = 80

    if tenure < 12 and monthly_charges > 70:

        prediction = "Customer likely to churn"

    else:

        prediction = "Customer will stay"

    save_prediction(
        tenure,
        monthly_charges,
        prediction
    )