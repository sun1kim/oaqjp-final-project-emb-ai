import requests
import json

def emotion_detector(text_to_analyze):
    # API Endpoint and Header
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input Text
    input_json = { "raw_document": { "text": text_to_analyze } }

    # POST request
    response = requests.post(url, headers=headers, json=input_json)

    # convert response text into a dictionary
    formatted_response = json.loads(response.text)

    # Extract required set of emotions
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

