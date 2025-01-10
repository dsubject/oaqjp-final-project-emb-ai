"""
This module defines a Flask application for detecting emotions in a given text.

The application exposes an endpoint `/emotionDetector` that processes input text
using the `EmotionDetection` module and returns the emotion scores and the dominant emotion.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

# Initialize Flask app
app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Endpoint to detect emotions in a given text.

    Returns:
        A JSON response with the emotion scores and dominant emotion
        or an error message if the input is invalid.
    """
    # Get json from request
    data = request.get_json()

    # Extract input text
    input_text = data['text']

    # Process text using the emotion detector
    result = emotion_detector(input_text)

   # Handle cases where dominant_emotion is None
    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Format response
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']['emotion']}."
    )

    return response

if __name__ == "__main__":
    # Run Flask app
    app.run(host="localhost", port=5000, debug=True)
