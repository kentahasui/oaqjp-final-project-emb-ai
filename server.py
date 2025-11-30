from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('__name__')

@app.route('/')
def get_index():
    return render_template("index.html")

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    text = request.args.get('textToAnalyze')
    if (text is None or text.strip() == ""):
        return "Please enter a non-empty string."
    
    emotions = emotion_detector(text)
    if (emotions is None):
        return "Invalid input. Please try again!"
    
    return f"For the given statement, the system response is " \
           f"'anger': {emotions['anger']}, " \
           f"'disgust': {emotions['disgust']}, " \
           f"'fear': {emotions['fear']}, " \
           f"'joy': {emotions['joy']}, and " \
           f"'sadness': {emotions['sadness']}. " \
           f"The dominant emotion is <b>{emotions['dominant_emotion']}</b>."

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)