from flask import Flask, request, send_file
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return 'TTS service is up! Send POST to /speak with JSON: { "text": "your message" }'

@app.route('/speak', methods=['POST'])
def speak():
    data = request.get_json()
    if not data or 'text' not in data:
        return {'error': 'Please provide "text" in JSON.'}, 400

    text = data['text']
    filename = f"output_{uuid.uuid4()}.mp3"
    tts = gTTS(text)
    tts.save(filename)

    return send_file(filename, mimetype="audio/mpeg", as_attachment=True), 200
