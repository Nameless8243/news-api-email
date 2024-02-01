import requests
from send_email import send_email

topic = "tesla"

api_key = "966300d61b64472c8cf694df9bb5b173"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-01-01&" \
      "sortBy=publishedAt&" \
      "apiKey=966300d61b64472c8cf694df9bb5b173&" \
      "language=en"

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][0:20]:
    title = article.get("title", "")
    description = article.get("description", "")
    url = article.get("url", "")
    if title and description:
        body += "Subject: Today's news" + "\n"\
                + title + "\n"\
                + description + "\n"\
                + url + "\n\n"

body = body.encode("utf-8")
send_email(body)
