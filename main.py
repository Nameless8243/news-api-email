import requests
from send_email import send_email

api_key = "966300d61b64472c8cf694df9bb5b173"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-01-01&sortBy=publishedAt&apiKey=" \
      "966300d61b64472c8cf694df9bb5b173"

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article titles and description
"""
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2*"\n"
"""

# Access the article titles and description
body = ""
for article in content["articles"]:
    title = article.get("title", "")
    description = article.get("description", "")
    if title and description:  # Check if both title and description exist
        body += title + "\n" + description + 2 * "\n"  # Concatenate title and description


body = body.encode("utf-8")
send_email(body)
