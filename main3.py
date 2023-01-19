import requests, json, os

newsKey = os.environ['newsapi']
country = "us"

url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}" # Typo in the URL

result = requests.get(url)
data = result.json()# Didn't format the data as json

for article in data['articles']:
  print(article['title'])
  print(article['url'])
  print(article['content'])