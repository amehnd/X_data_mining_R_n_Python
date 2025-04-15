import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

url = "https://api.twitter.com/2/users?ids=@realDonaldTrump&user.fields=affiliation,confirmed_email,connection_status,created_at,description,entities,id,is_identity_verified,location,most_recent_tweet_id,name,parody,pinned_tweet_id,profile_banner_url,profile_image_url,protected,public_metrics,receives_your_dm,subscription,subscription_type,url,username,verified,verified_followers_count,verified_type,withheld&expansions=most_recent_tweet_id"

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

response = requests.get(url, headers=headers)

# Save JSON to file
if response.status_code == 200:
    data = response.json()
    with open("twitter_users.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Data saved to twitter_users.json")
else:
    print("Request failed:", response.status_code)
