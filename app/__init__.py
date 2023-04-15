from flask import Flask
from app.classifier import api as emotion_classifier_api

app = Flask(__name__)

app.register_blueprint(emotion_classifier_api, url_prefix='/api')
