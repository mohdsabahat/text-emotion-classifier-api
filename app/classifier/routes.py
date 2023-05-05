from . import api
from flask import jsonify, request
from app.utils import load_model
import os

model_path = os.environ.get('EMOTION_CLASSIFIER_LOCATION')
#model_path = "E:/github/text-emotion-classifier-api/app/models/emotion-classifier-lr-23-04-2023.pkl"

model = load_model(model_path)

def predict_emot(text):

    global model

    int_to_emotion = {
            0: 'sadness', 1: 'joy', 2: 'love',
            3: 'anger', 4: 'fear', 5: 'surprise'
            }
    prediction = model.predict([text])
    return int_to_emotion.get(prediction[0]) #, 'undefined')


@api.route('/predict', methods=['GET', 'POST'])
def predict_emotion():
    print(request.form)
    print(request.args)
    input_text = request.args.get('input', '')
    resp = {}
    if input_text:
        predicted = predict_emot(input_text)
        resp["input"] = input_text
        resp["prediction"] = predicted
    else:
        resp["msg"] = "give some input"

    return jsonify(resp)
