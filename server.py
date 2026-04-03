"""
Flask server for Emotion Detection application.
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect():
    """
    This function takes user input text, calls the emotion detection function,
    and returns a formatted response with detected emotions and the dominant emotion.
    """
    text = request.args.get("textToAnalyze")

    result = emotion_detector(text)
    # ✅ Handle invalid input
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
