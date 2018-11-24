
from server.stewie import * 
import requests

headers  = {'Ocp-Apim-Subscription-Key': MICROSOFT_KEY, "Content-Type": "application/octet-stream" }

def get_image_emotion(image_path):
    image_data = open(image_path, "rb").read()
    response = requests.post(MICROSOFT_URL, headers=headers, data=image_data)
    response.raise_for_status()
    analysis = response.json()
    print(analysis)
    return analysis


if __name__ == '__main__':
    get_image_emotion()