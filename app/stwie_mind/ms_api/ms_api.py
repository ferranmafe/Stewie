
from app.stwie_mind import * 
import requests

headers  = {'Ocp-Apim-Subscription-Key': MICROSOFT_KEY, "Content-Type": "application/octet-stream" }

def get_image_emotion(image_url):
    image_path = "images/emotion_1.jpg"
    image_data = open(image_path, "rb").read()
    requests.post(emotion_recognition_url, headers=headers, data=image_data)
    response.raise_for_status()
    analysis = response.json()
    return analysis