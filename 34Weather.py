# API key allows you to check how often you are using the API and how much data you are pulling
# Get API key from https://home.openweathermap.org/users/sign_up

#TODO finish this app when valid credit card is available

import os

import requests
from twilio.rest import Client

# weather
OMW_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
apiKey = ""

weather_params = {
    "lat": 45.240372,
    "lon": 19.711800,
    "appid": apiKey,
}

data = requests.get(OMW_Endpoint, params=weather_params)

print(data.json())

current_weather = data.json()["weather"][0]["main"]

print(current_weather)

twilio
TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""

is_raining = False

if current_weather == "Rain":
    is_raining = True
    
account_sid = os.environ[TWILIO_ACCOUNT_SID]
auth_token = os.environ[TWILIO_AUTH_TOKEN]
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="The hail of heavens tears is attempting to flood the world today. Be prepared. Bring an umbrella ☔️. "
         " - 34Weather Forecast",
    from_="",
    to="",
)
