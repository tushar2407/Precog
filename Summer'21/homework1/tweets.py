import tweepy
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

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# print(api.me().name)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


csvFile = open('global_InternationalNursesDay.csv', 'w')
csvWriter = csv.writer(csvFile)
data = {'tweets':[]}
count = 0
for tweet in tqdm(tweepy.Cursor(api.search,q="#InternationalNursesDay",count=10000,
                           lang="en",
                           since="2020-05-13").items()):
    # print (tweet.created_at, tweet.text)
    # print(type(tweet))
    # file = open("tweet.txt", "w+")
    # file.write(str(tweet))
    # break
    csvWriter.writerow([
        tweet.created_at, tweet.text.encode('utf-8'), tweet.user.id, tweet.user.name
    ])
    data['tweets'].append(tweet)
    count+=1
    if(count==10000):
        break
#     data.append([
#         tweet.created_at, tweet.text.encode('utf-8'), tweet.user.id, tweet.user.name
#     ])
# df = pd.DataFrame(data, columns = ['CreatedAt', 'tweets', 'user_id', 'user_name'])
# import json
# with open("global_InternationNursesDay.json", "w") as f:
#     json.dump(data, f)
#     f.close()