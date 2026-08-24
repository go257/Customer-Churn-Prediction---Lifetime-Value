import psycopg2


def get_connection():

    return psycopg2.connect(
        host="localhost",
        database="customer_churn_db",
        user="postgres",
        password="Prasanta@2005",
        port="5432"
    )


try:

    print("====================================")
    print(" CUSTOMER CHURN PROJECT")
    print(" FINAL DATABASE REPORT")
    print("====================================")

    conn = get_connection()
    cur = conn.cursor()

    # Total records
    cur.execute("""
        SELECT COUNT(*)
        FROM prediction_history
    """)

    total = cur.fetchone()[0]

    # Average tenure
    cur.execute("""
        SELECT AVG(tenure)
        FROM prediction_history
    """)

    avg_tenure = cur.fetchone()[0]

    # Average charges
    cur.execute("""
        SELECT AVG(monthly_charges)
        FROM prediction_history
    """)

    avg_charges = cur.fetchone()[0]

    # Prediction summary
    cur.execute("""
        SELECT prediction, COUNT(*)
        FROM prediction_history
        GROUP BY prediction
    """)

    predictions = cur.fetchall()

    print("\nTotal Predictions:", total)

    print(
        "Average Tenure:",
        round(avg_tenure, 2) if avg_tenure else 0
    )

    print(
        "Average Monthly Charges:",
        round(avg_charges, 2) if avg_charges else 0
    )

    print("\nPrediction Summary:")

    for prediction, count in predictions:

        print(
            f"{prediction}: {count}"
        )

    print("\nDatabase Connection: SUCCESS")
    print("Project Status: COMPLETED")

    cur.close()
    conn.close()

except Exception as e:

    print("\nProject Error:")
    print(e)