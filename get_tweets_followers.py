
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

def get_all_tweets(screen_name, user):
    
    alltweets = []  
    try:
        new_tweets = api.user_timeline(screen_name = screen_name,count=20)
        for i in new_tweets:
            if "#MasterTrailer" in i.text:
                alltweets.append(i)
        try:
            oldest = alltweets[-1].id - 1
        except:
            return
        outtweets = [[user, tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]
        with open(f'follower_tweets.csv', 'a+') as f:
            writer = csv.writer(f)
            # writer.writerow(["user_id","follower_id","created_at","text"])
            writer.writerows(outtweets)
    except:
        # print("User {} has protected tweets so can't access")
        pass
    
file = open("list_followers.txt", "r")

lines = file.readlines()

with open(f'follower_tweets.csv', 'w+') as f:
    writer = csv.writer(f)
    writer.writerow(["user_id","follower_id","created_at","text"])
    # writer.writerows(outtweets)

for i in tqdm(range(0,len(lines),2)):
    user, followers = lines[i], eval(lines[i+1])
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    # auth.set_access_token(access_token, access_token_secret) 
    # api = tweepy.API(auth) 
    for follower in tqdm(followers[:20]):
        try:
            screen_name = api.get_user(follower).screen_name
            get_all_tweets(screen_name, user)
        except:
            pass