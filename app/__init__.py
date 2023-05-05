from flask import Flask, render_template, url_for
from app.classifier import api as emotion_classifier_api
import os

EMOTION_CLASSIFIER_LOCATION = os.environ.get('EMOTION_CLASSIFIER_LOCATION') # Absolute path to .pkl file
#EMOTION_CLASSIFIER_LOCATION="E:\github\text-emotion-classifier-api\app\models\emotion-classifier-lr-23-04-2023.pkl"
app = Flask(__name__)

if not os.path.exists(EMOTION_CLASSIFIER_LOCATION):
    print('Path to the model does not exists')

app.register_blueprint(emotion_classifier_api, url_prefix='/api/emotion_classifier')

@app.route('/')
def home():
    return render_template('index.html')
