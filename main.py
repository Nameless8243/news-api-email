import requests

api_key = "966300d61b64472c8cf694df9bb5b173"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-01-01&sortBy=publishedAt&apiKey=" \
      "966300d61b64472c8cf694df9bb5b173"

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])