import tweepy
import csv
consumer_key="AFmamfGy4208xqZNLqIDJiq4D"
consumer_secret="yLsACdN5yfcV6KiNf4CP3STqSsYMonkiw3j8hTzMGyyqFdGxQM"

access_token="1278403366201159680-Eh3s9MCHT28bFzOFlXWKZydtwdGl8L"
access_token_secret="vHeseRGYju6BS9pfCeAYmjNFF7kGQ5MSAuxhx9MH5pLMc"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print(api.me().name)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
csvFile = open('ua.csv', 'a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#medicaid",count=1000,
                           lang="en",
                           since="2020-12-03").items():
    # print (tweet.created_at, tweet.text)
    print(type(tweet))
    file = open("tweet.txt", "w+")
    file.write(str(tweet))
    break
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])