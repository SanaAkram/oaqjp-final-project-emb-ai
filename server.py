"""
Flask server for Emotion Detection application.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def detect():
    """
    Handle emotion detection requests.

    Returns:
        JSON response with detected emotions.
    """
    text = request.args.get("textToAnalyze")

    if not text:
        return "Invalid input", 400

    result = emotion_detector(text)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
