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

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM prediction_history
        ORDER BY id DESC
    """)

    rows = cur.fetchall()

    print("\n========== PREDICTION HISTORY ==========\n")

    if len(rows) == 0:

        print("No prediction records found.")

    else:

        for row in rows:
            print(
                "ID:", row[0],
                "| Tenure:", row[1],
                "| Monthly Charges:", row[2],
                "| Prediction:", row[3]
            )

    cur.close()
    conn.close()

except Exception as e:

    print("Database Error:")
    print(e)