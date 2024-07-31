""" Module providing Flask, render_template,request """

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")


@app.route("/")
def home():
    """retrn home page"""
    return render_template("index.html")


@app.route("/emotionDetector")
def get_emotion_detect_result():
    """return emotion detect result"""
    text_to_analyse = request.args.get("textToAnalyze")
    if len(text_to_analyse) == 0 or text_to_analyse.isspace():
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is 'anger': {result['anger']},
     'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and
     'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."""


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
