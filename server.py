from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    # Renders the main application interface
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    # Retrieves the text from the HTML interface
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Passes the text to the application function
    response = emotion_detector(text_to_analyze)
    
    # Formats the response into the required string
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    # Runs the application on localhost:5000
    app.run(host="0.0.0.0", port=5000)