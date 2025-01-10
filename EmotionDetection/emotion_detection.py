import requests
import json

def emotion_detector(text_to_analyze):
    # API endpoint and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    # Input JSON
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Send POST request
        response = requests.post(url, json=myobj, headers=headers)

        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

        res = response.json()

        # Extract emotions dictionary
        formatted_response = res['emotionPredictions'][0]['emotion']

        # Find dominant emotion (emotion w/ highest score)
        dominant_emotion = max(formatted_response.items(), key=lambda x: x[1])

        # Add dominant emotion to response
        formatted_response['dominant_emotion'] = {"emotion": dominant_emotion[0], "score": dominant_emotion[1]}

        return formatted_response

    except Exception as e:
        return {"error": str(e)}