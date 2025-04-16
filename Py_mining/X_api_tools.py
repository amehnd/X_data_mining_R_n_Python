import requests
import json
from dotenv import load_dotenv
import os
import time 
load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
# print(f"Bearer Token: {BEARER_TOKEN}")

url = "https://api.twitter.com/2/users/by/username/realdonaldtrump?user.fields=created_at,description,most_recent_tweet_id"

headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

while True:
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    if response.status_code == 200:
        data = response.json()
        with open("twitter_users.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved to twitter_users.json")
        break  

    elif response.status_code == 429:
        print(" Rate limit hit! Waiting 24 hours before retrying...")
        time.sleep( 24 * 60 * 60)  
        continue  

    else:
        print("Request failed:", response.status_code)
        print("Response:", response.text)
        break 