import datetime as dt

import requests

MY_LAT = 11.127123
MY_LONG = 78.656891
# response = requests.get(url="https://api.kanye.rest/")
# response.raise_for_status()
#
# print(response.json())
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)


parameters = {"lat": MY_LAT,
              "long": MY_LONG,
              "formatted": 0}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
print(response.json())

sunrise = response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]
time_now = dt.datetime.now()
print(sunset.split("T")[1].split(":")[0])
print(sunrise.split("T")[1].split(":")[0])
