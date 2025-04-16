import requests
from bs4 import BeautifulSoup
import json

# Define the search query
query = "Statue of Liberty site:twitter.com"
url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

# Set the headers to mimic a real browser request (bypasses bot protection)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Make a request to Google search page
response = requests.get(url, headers=headers)

# Parse the response with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the tweet links
results = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')

# Collect tweet texts into a list
tweets = [result.text for result in results]
print(tweets)
# Save the tweets to a JSON file
with open('tweets.json', 'w') as f:
    json.dump(tweets, f)

print("Tweets saved to tweets.json")
