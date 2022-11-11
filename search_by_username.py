import os
import tweepy
from dotenv import load_dotenv


load_dotenv()

client = tweepy.Client(bearer_token = os.getenv('BEARER_TOKEN'))

username = input("Enter the username you want to search: ")

response = client.get_user(username=username, user_fields=["profile_image_url", "description", "created_at", "location", "protected", "public_metrics", "url"])

user = response.data
k = "name"
for key, value in user.items():
    key = str(key).replace("_", " ").capitalize()
    print(f"{key} - {value}")
