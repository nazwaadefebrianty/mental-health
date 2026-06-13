import joblib

model = joblib.load("models/decision_tree/decision_tree.joblib")
scaler = joblib.load("models/decision_tree/scaler.joblib")

def predict_dt(data):
    scaled_data = scaler.transform([data])
    prediction = model.predict(scaled_data)
    return prediction[0]