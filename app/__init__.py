from flask import Flask
from app.classifier import api as emotion_classifier_api
import os

EMOTION_CLASSIFIER_LOCATION = os.environ.get('EMOTION_CLASSIFIER_LOCATION') # Absolute path to .pkl file

app = Flask(__name__)

if not os.path.exists(EMOTION_CLASSIFIER_LOCATION):
    print('Path to the model does not exists')

app.register_blueprint(emotion_classifier_api, url_prefix='/api/emotion_classifier')
