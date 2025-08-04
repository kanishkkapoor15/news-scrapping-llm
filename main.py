import os
import requests
import pandas as pd
from dotenv import load_dotenv

#loading api key

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

url="https://newsapi.org/v2/top-headlines"

params = {
    "country": "us",
    "category": "technology",
    "pageSize": 20,
    "apiKey": API_KEY
}

#fetch data

response = requests.get(url, params=params)
data = response.json()

#extract relevant fields

articles = data.get("articles", [])
records= []
for article in articles:
    records.append({
        "source": article["source"]["name"],
        "title": article["title"],
        "description": article["description"],
        "content": article["content"],
        "publishedAt": article["publishedAt"],
        "url": article["url"]
    })

#save to csv
df = pd.DataFrame(records)
df.to_csv("data/news_raw.csv", index=False)
print("✅ News data saved to data/news_raw.csv")