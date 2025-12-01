"""Flask application for emotion analysis service."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('__name__')

@app.route('/')
def get_index():
    """Serves the index page of the application."""
    return render_template("index.html")

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    """Detects the emotions in the textToAnalyze query parameter.
    
       Returns a string describing the emotions, as well as 
       the dominant emotion.
    """
    text = request.args.get('textToAnalyze')

    emotions = emotion_detector(text)
    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is " \
           f"'anger': {emotions['anger']}, " \
           f"'disgust': {emotions['disgust']}, " \
           f"'fear': {emotions['fear']}, " \
           f"'joy': {emotions['joy']}, and " \
           f"'sadness': {emotions['sadness']}. " \
           f"The dominant emotion is <b>{emotions['dominant_emotion']}</b>."

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
