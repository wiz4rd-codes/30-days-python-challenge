import requests
print("==============FILMRADAR==============")
movie_name = input("Enter name of the movie : ")
api_key = input("Enter your api key : ")
url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"

response = requests.get(url)
data = response.json()

if data.get("Response") == "False":
    print(f"Error: {data.get('Error')}")
else:
    for key , value in data.items(): 
        print(f"{key} : {value}")
