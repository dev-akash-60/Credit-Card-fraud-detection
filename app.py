from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained components
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        step = float(request.form["step"])
        type_input = request.form["type"]
        amount = float(request.form["amount"])
        oldbalanceOrg = float(request.form["oldbalanceOrg"])
        newbalanceOrig = float(request.form["newbalanceOrig"])
        oldbalanceDest = float(request.form["oldbalanceDest"])
        newbalanceDest = float(request.form["newbalanceDest"])

        # Encode categorical feature
        type_encoded = encoder.transform([type_input])[0]

        # Prepare input
        features = np.array([[step, type_encoded, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]])

        # Scale
        features_scaled = scaler.transform(features)

        # Predict
        prediction_proba = model.predict_proba(features_scaled)[0][1]
        prediction = model.predict(features_scaled)[0]

        risk_score = round(prediction_proba * 100, 2)
        color = "red" if prediction == 1 else "green"
        text = f"🚨 High Risk Transaction Detected! (Risk: {risk_score}%)" if prediction == 1 else f"✅ Low Risk Transaction (Risk: {risk_score}%)"

        return render_template("index.html", prediction_text=text, probability=risk_score, color=color)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}", probability=0, color="gray")

if __name__ == "__main__":
    app.run(debug=True)
