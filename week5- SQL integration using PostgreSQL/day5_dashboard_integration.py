from flask import Flask, render_template
import psycopg2

app = Flask(__name__)


def get_connection():

    return psycopg2.connect(
        host="localhost",
        database="customer_churn_db",
        user="postgres",
        password="Prasanta@2005",
        port="5432"
    )


@app.route("/")
def dashboard():

    try:

        conn = get_connection()
        cur = conn.cursor()

        # Total predictions
        cur.execute("""
            SELECT COUNT(*)
            FROM prediction_history
        """)

        total = cur.fetchone()[0]

        # Stay customers
        cur.execute("""
            SELECT COUNT(*)
            FROM prediction_history
            WHERE LOWER(prediction) LIKE '%stay%'
        """)

        stay = cur.fetchone()[0]

        # Churn customers
        cur.execute("""
            SELECT COUNT(*)
            FROM prediction_history
            WHERE LOWER(prediction) LIKE '%churn%'
        """)

        churn = cur.fetchone()[0]

        # All records
        cur.execute("""
            SELECT *
            FROM prediction_history
            ORDER BY id DESC
        """)

        records = cur.fetchall()

        cur.close()
        conn.close()

        return render_template(
            "dashboard.html",
            total=total,
            stay=stay,
            churn=churn,
            records=records
        )

    except Exception as e:

        return f"Database Error: {e}"


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )