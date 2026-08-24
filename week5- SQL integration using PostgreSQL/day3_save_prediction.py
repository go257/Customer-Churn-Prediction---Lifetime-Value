import psycopg2


def get_connection():

    return psycopg2.connect(
        host="localhost",
        database="customer_churn_db",
        user="postgres",
        password="Prasanta@2005",
        port="5432"
    )


# Example prediction values
tenure = 30
monthly_charges = 70.50
prediction = "Customer will stay"


try:

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS prediction_history (
            id SERIAL PRIMARY KEY,
            tenure FLOAT,
            monthly_charges FLOAT,
            prediction VARCHAR(100)
        )
    """)

    cur.execute("""
        INSERT INTO prediction_history
        (tenure, monthly_charges, prediction)
        VALUES (%s, %s, %s)
    """, (
        tenure,
        monthly_charges,
        prediction
    ))

    conn.commit()

    print("Prediction Saved Successfully!")

    cur.close()
    conn.close()

except Exception as e:

    print("Error:")
    print(e)