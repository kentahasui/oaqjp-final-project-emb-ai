import json
import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 

def emotion_detector(text):
    """Detects emotion of the given text using Watson AI libraries."""
    if text is None or text.strip() == "":
        return None
    
    payload = {
        "raw_document": {
            "text": text
        }
    }

    response = requests.post(
        URL,
        headers = HEADERS,
        json = payload)
    
    if (response.status_code != 200):
        return None
    
    formatted_response = json.loads(response.text)
    predictions = formatted_response['emotionPredictions']
    if (len(predictions) == 0): 
        return None
    
    return predictions[0]['emotion']

if __name__ == "__main__":
    response = emotion_detector("I love everything")
    print(response)
