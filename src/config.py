import os
import tweepy
from dotenv import load_dotenv


load_dotenv()

client = tweepy.Client(bearer_token = os.getenv('BEARER_TOKEN'))

auth = tweepy.OAuth2BearerHandler(os.getenv('BEARER_TOKEN'))
api = tweepy.API(auth)