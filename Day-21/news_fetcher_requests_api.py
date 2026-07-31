import requests
from datetime import date,timedelta
categories = ["Technology","Business","Sports","Entertainment","Health","Science"]
print("=======TOP CATEGORIES=======")
for i,category in enumerate(categories, start =1 ):
    print(f"{i}. {category}")

in_category = input("Enter Category you choose or any other category : ")
api_key = input("Enter your api key : ")
news_date = date.today() - timedelta(days=7)


url = f"https://newsapi.org/v2/everything?q={in_category}&from={news_date}&sortBy=publishedAt&apiKey={api_key}"
response = requests.get(url)

data = response.json()
print("===========================================HEADLINES===========================================")
for i, article in enumerate(data["articles"],start = 1):
    print(f"\nNews {i} : ")
    print("Title : ",article["title"])
    print("Description : ",article["description"])
    print("Source : ",article["source"]["name"])
    print("Published At : ",article["publishedAt"])
    print()
    
