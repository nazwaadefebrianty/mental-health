import joblib

model = joblib.load("models/svm/svm.pkl")
scaler = joblib.load("models/svm/scaler.pkl")

def predict_svm(data):
    scaled_data = scaler.transform([data])
    prediction = model.predict(scaled_data)
    return prediction[0]