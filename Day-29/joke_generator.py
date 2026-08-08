import requests
import time
print("================JOKE GENERATOR==============")
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)
data = response.json()
print(f"{data['setup']}")
time.sleep(2)
print(f"{data['punchline']}")
