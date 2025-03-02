import requests
import os
from datetime import datetime


# Nutritionix API
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Constants
GENDER = YOUR GENDER
WEIGHT_KG = YOUR WEIGHT
HEIGHT_CM = YOUR HEIGHT
AGE = YOUR AGE

APP_ID = os.environ["YOUR_APP_ID"]
APP_KEY = os.environ["YOUR_API_KEY"]

# Sheety API
SHEETY_ENDPOINT = os.environ["YOUR_SHEET_ENDPOINT"]
SHEETY_TOKEN = os.environ["YOUR_SHEET_TOKEN"]


headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_params, headers=headers)
result=response.json()
print(result)

# Spreadsheet data
date = datetime.now()
time = date.strftime("%X")
date_f = date.strftime("%d/%m/%Y")

auth_header = {
    "Authorization": "Bearer " + SHEETY_TOKEN
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date_f,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=auth_header)
    print(response.text)





