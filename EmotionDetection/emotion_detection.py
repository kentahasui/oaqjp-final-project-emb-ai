from collections import defaultdict
import json
import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 

def emotion_detector(text):
    """Detects emotion of the given text using Watson Emotion Prediction AI library.
       
       Args: 
         text (str): Text to process
        Returns: 
          A dictionary with emotion names as keys and emotion scores as values
    """
    payload = {"raw_document": {"text": text}}

    response = requests.post(
        URL,
        headers = HEADERS,
        json = payload)

    if (response.status_code == 400):
        return defaultdict(lambda: None)
    
    formatted_response = json.loads(response.text)
    predictions = formatted_response['emotionPredictions']
    if (len(predictions) == 0): 
        return defaultdict(lambda: None)
    
    emotions = predictions[0]['emotion']
    emotions['dominant_emotion'] = _get_dominant_emotion(emotions)
    return emotions


def _get_dominant_emotion(emotions):
    """Returns the emotion with the highest score.

    Args:
      emotions (dict): A dictionary with emotion names as keys and a numerical score as values.
    Returns: 
      The emotion (str) with the highest score
    """
    return max(emotions, key=emotions.get)

if __name__ == "__main__":
    response = emotion_detector("I both love and hate the opera")
    print(response)
