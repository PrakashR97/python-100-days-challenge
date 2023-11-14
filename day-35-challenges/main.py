import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = '69737d617e71d09242d7004b068b2238'

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()["weather"][:12]
print(weather_data[0]["id"])
weather = [weather["id"] for weather in weather_data]

for i in weather:
    if i > 500:
        print("bring the umbrella")
    account_sid = 'AC46071ada92fba1d9566a421d174d376c'
    auth_token = '480595474a809050b7e87a7a9d056fac'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hey Thiru Bastard ❤️",
        from_='+12569803927',
        to='+919698710360'
    )
    print(message.status)
