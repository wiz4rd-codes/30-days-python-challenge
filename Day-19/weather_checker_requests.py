import requests

print("========== WEATHER CHECKER ==========")

city = input("Enter City : ")
url = f"https://wttr.in/{city.capitalize()}?format=j1"

response = requests.get(url)

data = response.json()

print(f'Temperature : {data["current_condition"][0]['temp_C']} C')
print(f"Humidity : {data["current_condition"][0]['humidity']}")
print(f'Chance of Rain : {data["weather"][0]["hourly"][0]["chanceofrain"]}')
print(f"Wind Speed : {data["current_condition"][0]['windspeedMiles']}")
