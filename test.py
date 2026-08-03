import joblib

model = joblib.load(
    "models/emotion_classifier.pkl"
)

label_encoder = joblib.load(
    "models/label_encoder.pkl"
)


text = "I am extremely happy today!"

prediction = model.predict([text])[0]

emotion = label_encoder.inverse_transform(
    [prediction]
)[0]

print("Prediction:", prediction)
print("Emotion:", emotion)