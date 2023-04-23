from . import api
from flask import jsonify, request
from app.utils import load_model
import os

model_path = os.environ.get('EMOTION_CLASSIFIER_LOCATION')

model = load_model(model_path)

def predict_emotion(text):

    global model

    int_to_emotion = {
            0: 'sadness', 1: 'joy', 2: 'love',
            3: 'anger', 4: 'fear', 5: 'surprise'
            }
    prediction = model.predict(text)
    return int_to_emotion.get(prediction) #, 'undefined')


@api.route('/predict', methods=['POST'])
def predict_emotion():
    input_text = request.form.get('input', '')
    resp = {"msg": "dummy data"}
    if input_text:
        predicted = predict_emotion(input_text)
        resp["input"] = input_text
        resp["prediction"] = predicted
    else:
        resp["msg"] = "give some input"

    return jsonify(resp)
