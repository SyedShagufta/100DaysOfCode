from datetime import datetime
from requests.auth import HTTPBasicAuth
import requests
import os

ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/ceab2dee5bf4d021066960cf2afcacd3/workoutTracking/workouts"

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]


header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

sentence = input("Tell me what exercises you did: ")

params = {
    "query": sentence,
}

today = datetime.now()
date = today.strftime("%d/%m/%Y")
basic = HTTPBasicAuth('sofia26', 'Sofia2602')

response = requests.post(url=ENDPOINT, json=params, headers=header)
data = response.json()
now_time = datetime.now().strftime("%X")
for exercise in data["exercises"]:
    sheet_params = {
        "workout": {
            "date": date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_params, auth=basic)
    # print(sheet_params)
