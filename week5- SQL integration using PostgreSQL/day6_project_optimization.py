import psycopg2


def get_connection():

    return psycopg2.connect(
        host="localhost",
        database="customer_churn_db",
        user="postgres",
        password="  Prasanta@2005",
        port="5432"
    )


try:

    conn = get_connection()
    cur = conn.cursor()

    print("========== PROJECT OPTIMIZATION ==========")

    # Total records
    cur.execute("""
        SELECT COUNT(*)
        FROM prediction_history
    """)

    total = cur.fetchone()[0]

    print("\nTotal Predictions:", total)

    # Average tenure
    cur.execute("""
        SELECT AVG(tenure)
        FROM prediction_history
    """)

    avg_tenure = cur.fetchone()[0]

    print(
        "Average Tenure:",
        round(avg_tenure, 2) if avg_tenure else 0
    )

    # Average monthly charges
    cur.execute("""
        SELECT AVG(monthly_charges)
        FROM prediction_history
    """)

    avg_charges = cur.fetchone()[0]

    print(
        "Average Monthly Charges:",
        round(avg_charges, 2) if avg_charges else 0
    )

    # Prediction summary
    cur.execute("""
        SELECT prediction, COUNT(*)
        FROM prediction_history
        GROUP BY prediction
        ORDER BY COUNT(*) DESC
    """)

    results = cur.fetchall()

    print("\nPrediction Summary:")

    for prediction, count in results:

        print(
            prediction,
            ":",
            count
        )

    cur.close()
    conn.close()

    print("\nOptimization Completed Successfully!")

except Exception as e:

    print("Error:")
    print(e)