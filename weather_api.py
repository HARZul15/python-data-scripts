import requests

response = requests.get("https://wttr.in/Kandy?format=j1")

data = response.json()

current = data["current_condition"][0]

print(f"Weather in Kandy: \nTemperature: {current['temp_C']}°C \nFeels like: {current['FeelsLikeC']}°C \nCondition: {current['weatherDesc'][0]['value']} \nHumidity: {current['humidity']} \nWind Speed: {current['windspeedKmph']}km/h")