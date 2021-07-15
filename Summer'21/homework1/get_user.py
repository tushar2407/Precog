import tweepy
import requests
import csv
from tqdm import tqdm
import os
# import  pandas as pd
from dotenv import load_dotenv
load_dotenv()

consumer_key=os.getenv("CONSUMER_KEY")
consumer_secret=os.getenv("CONSUMER_SECRET")

access_token=os.getenv("ACCESS_TOKEN")
access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")

bearer_token = os.getenv("BEARER_TOKEN")

# response = requests.get("https://api.twitter.com/labs/2/users/2420638080", headers = {
#     "Authorization" : f"Bearer {bearer_token}"
# })
# print(response.json())

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


print(api.get_user("SinghAphrodite")._json)
  
