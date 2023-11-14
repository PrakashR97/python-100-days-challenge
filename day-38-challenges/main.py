import requests
from datetime import datetime

API_KEY = "4ce5cb2b8410adcbd63fc540e1069fc7"
APP_ID = "3f630aa1"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


dt = datetime.now()
date = dt.strftime("%d-%b-%y")
time = dt.strftime("%I:%M:%S")


data = {
    "query": "iam doing cardio 30 minutes on everyday",
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=exercise_endpoint, json=data, headers=headers)
# print(response.json())

google_sheet_endpoint = "https://api.sheety.co/3ddf4daef76ae5d20d0dc2b09796469c/myWorkouts/sheet1"

# data = response.json()["exercises"][0]
name = response.json()["exercises"][0]["name"]
nf_calories = response.json()["exercises"][0]["nf_calories"]
duration_min = response.json()["exercises"][0]["duration_min"]
print(name, nf_calories, duration_min)

user_data = {
    "sheet1": {
        "date": date,
        "time": time,
        "exercise": name,
        "duration": duration_min,
        "calories": nf_calories}
}
google_sheets_headers = {
    "Authorization": "Bearer YOUR_GOOGLE_SHEETS_ACCESS_TOKEN",  # Replace with your actual access token
    "Content-Type": "application/json"
}

google_sheet_response = requests.post(url=google_sheet_endpoint, json=user_data, headers=google_sheets_headers)

print(google_sheet_response.json())
