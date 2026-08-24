import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="customer_churn_db",
        user="postgres",
        password="Prasanta@2005",
        port="5432"
    )

    print("Connected Successfully!")

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS prediction_history (
            id SERIAL PRIMARY KEY,
            tenure FLOAT,
            monthly_charges FLOAT,
            prediction VARCHAR(100)
        )
    """)

    conn.commit()

    print("Table Created Successfully!")

    cur.close()
    conn.close()

except Exception as e:
    print("Connection Error:")
    print(e)