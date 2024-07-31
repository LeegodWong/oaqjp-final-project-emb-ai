import requests
import json


def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=obj, headers=header)
    result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }
    if response.status_code == 400:
        return result
    else:
        emotion = json.loads(response.text)["emotionPredictions"][0]["emotion"]
        result["anger"] = emotion["anger"]
        result["disgust"] = emotion["disgust"]
        result["fear"] = emotion["fear"]
        result["joy"] = emotion["joy"]
        result["sadness"] = emotion["sadness"]
        result["dominant_emotion"] = max(emotion, key=emotion.get)
        return result
