from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("house_price_model.pkl")

# Example feature names (update based on your dataset's final features)
feature_names = joblib.load("feature_names.pkl")  # Optional: save & load column names if needed

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input values from form
        features = [float(x) for x in request.form.values()]
        final_features = np.array(features).reshape(1, -1)
        prediction = model.predict(final_features)[0]

        return render_template('result.html', prediction_text=f"Estimated Price: ₹{prediction:.2f} Lakhs")
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
