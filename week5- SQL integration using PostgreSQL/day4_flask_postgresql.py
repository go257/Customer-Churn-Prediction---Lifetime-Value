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
def home():

    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    try:

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, tenure, monthly_charges, prediction
            FROM prediction_history
            ORDER BY id DESC
        """)

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return render_template(
            "dashboard.html",
            records=rows
        )

    except Exception as e:

        return f"Database Error: {e}"


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )