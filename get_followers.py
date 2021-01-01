# import the module 
import tweepy 
from dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd
from tqdm import tqdm
import csv
import time
consumer_key = os.getenv("CONSUMER_KEY") 
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

csvFile = open('followers_tweets.csv', 'w')
csvWriter = csv.writer(csvFile)

file = open("unique_users.txt", "r")

lines = file.readlines()

file = open("list_followers.txt", "w+")

for line in tqdm(lines):
    line = int(line.strip())
    id = line
    ids = []
    # print(id)
    try:
        screen_name = api.get_user(id).screen_name
        for page in tweepy.Cursor(api.followers_ids, str(id)).items():
            ids.append(page)
            # time.sleep(60)
        file.write(str(line)+"\n")
        file.write(str(ids)+"\n")
        file.close()
        file = open("list_followers.txt", "a+")
    except:
        pass
    # for follower in api.followers(screen_name): 
	#     print(follower.screen_name) 
file.close()