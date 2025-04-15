import requests
import json
from dotenv import load_dotenv
import os
import time 
load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

url = "https://api.twitter.com/2/users?ids=realDonaldTrump&user.fields=created_at,description,pinned_tweet_id"

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

response = requests.get(url, headers=headers)

while True:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        with open("twitter_users.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved to twitter_users.json")
        break  

    elif response.status_code == 429:
        print(" Rate limit hit! Waiting 15 minutes before retrying...")
        time.sleep(15 * 60)  
        continue  

    else:
        print("Request failed:", response.status_code)
        print("Response:", response.text)
        break 