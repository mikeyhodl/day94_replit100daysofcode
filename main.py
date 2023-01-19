import os, requests, json, openai

news = os.environ['news']
openai.organisation = os.environ['organisationID']
openai.api_key = os.environ['openai']
openai.Model.list()

country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news}"

result = requests.get(url)
data = result.json()

counter = 0
for article in data["articles"]:
  counter += 1
  if counter > 5:
    break
  prompt = (f"""Summarise {article["url"]} in one sentence.""")
  response = openai.Completion.create(model="text-davinci-002",
                                      prompt=prompt,
                                      temperature=0,
                                      max_tokens=50)
  print(response["choices"][0]["text"].strip())