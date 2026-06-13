import joblib

model = joblib.load("models/knn/knn.pkl")
scaler = joblib.load("models/knn/scaler.pkl")

def predict_knn(data):
    scaled_data = scaler.transform([data])
    prediction = model.predict(scaled_data)
    return prediction[0]