from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Customer Churn Prediction API is running"


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        tenure = float(data["tenure"])
        monthly_charges = float(data["monthly_charges"])

        # Prediction logic
        if tenure < 12 and monthly_charges > 70:
            prediction = "Customer likely to churn"
        else:
            prediction = "Customer will stay"

        # LTV
        ltv = tenure * monthly_charges

        return jsonify({
            "tenure": tenure,
            "monthly_charges": monthly_charges,
            "prediction": prediction,
            "ltv": round(ltv, 2)
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )