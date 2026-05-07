"""Emotion Detection module."""

import json

import requests

def emotion_detector(text_to_analyze):
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id": 
        "emotion_aggregated-workflow_lang_en_stock"
    }

    request_body = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(
            url,
            json=request_body,
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:
            formatted_response = json.loads(response.text)
            # Extract emotion scores
            emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]

            # Find dominant emotion
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            emotion_scores['dominant_emotion'] = dominant_emotion
            return emotion_scores

    except requests.RequestException:
        pass

    return None
