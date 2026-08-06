import requests
print("==============GITSCAN==============")
username = input("Enter username : ")
url = f"https://api.github.com/users/{username}"
response = requests.get(url)
data = response.json()
if response.status_code != 200:
    print("User not found!")
else:
    keys_list = ["login","name","bio","public_repos","followers","following","location","company","blog","twitter_username","created_at","html_url"]
    for key in keys_list:
        print(f"{key} : {data[key]}")
