from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        tenure = float(request.form["tenure"])
        monthly_charges = float(request.form["monthly_charges"])

        if tenure < 12 and monthly_charges > 70:
            prediction = "Customer likely to churn"
        else:
            prediction = "Customer will stay"

        ltv = tenure * monthly_charges

        return render_template(
            "result.html",
            tenure=tenure,
            monthly_charges=monthly_charges,
            prediction=prediction,
            ltv=round(ltv, 2)
        )

    except Exception as e:

        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)