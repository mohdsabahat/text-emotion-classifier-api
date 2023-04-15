from . import api
from flask import jsonify, request

@api.route('/predict', methods=['POST'])
def predict_emotion():
    input_text = request.form.get('input', '')
    resp = {"msg": "dummy data"}
    if input_text:
        #predicted = predict_emotion(input_text)
        resp["input"] = input_text
    else:
        resp["msg"] = "give some input"

    return jsonify(resp)
