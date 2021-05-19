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


c = tweepy.Cursor(api.followers, 2420638080)
  
# counting the number of followers
# count = 0
# for follower in c.items(5):
#     count += 1
#     print(count)
import json

with open("friends.json", "w") as f:
	json.dump({
		"2420638080" : [
			i._json for i in c.items()
		]
	}, f)
# for i in c.items():
#     print(i._json)
#     break
# print(str(2420638080) + " has " + str(sum(1 for i in c.items())) + " followers.")




# csvFile = open('india_PalestineBleeding.csv', 'w')
# csvWriter = csv.writer(csvFile)
# # data = []
# for tweet in tqdm(tweepy.Cursor(api.search,q="#PalestineBleeding",count=10000,
#                            lang="en",
#                            since="2020-05-13").items()):
#     # print (tweet.created_at, tweet.text)
#     # print(type(tweet))
#     # file = open("tweet.txt", "w+")
#     # file.write(str(tweet))
#     # break
#     csvWriter.writerow([
#         tweet.created_at, tweet.text.encode('utf-8'), tweet.user.id, tweet.user.name
#     ])
#     data.append([
#         tweet.created_at, tweet.text.encode('utf-8'), tweet.user.id, tweet.user.name
#     ])
# df = pd.DataFrame(data, columns = ['CreatedAt', 'tweets', 'user_id', 'user_name'])



# User(_api=<tweepy.api.API object at 0x0000011912647160>, _json={'id': 1382609657429037059, 'id_str': '1382609657429037059', 'name': 'Aman Rajput', 
# 'screen_name': 'AmanRaj13635379', 'location': '', 'description': 'Aman Rajput', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 8, 'friends_count': 73, 'listed_count': 0, 'created_at': 'Thu Apr 15 08:20:19 +0000 2021', 'favourites_count': 5, 'utc_offset': None, 'time_zone': None, 'geo_enabled': 
# False, 'verified': False, 'statuses_count': 1, 'lang': None, 'status': {'created_at': 'Tue Apr 27 
# 09:34:04 +0000 2021', 'id': 1386976933083115522, 
# 'id_str': '1386976933083115522', 'text': '@myogioffice @myogiadityanath Allah ham sab ko is bimari se mhefujh rakhe https://t.co/NHtxi4tWMt', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'myogioffice', 'name': 'Yogi Adityanath Office', 'id': 1084769827271598080, 'id_str': '1084769827271598080', 'indices': [0, 12]}, {'screen_name': 'myogiadityanath', 'name': 'Yogi Adityanath', 'id': 3437532637, 'id_str': '3437532637', 'indices': [13, 
# 29]}], 'urls': [], 'media': [{'id': 1386976920722546697, 'id_str': '1386976920722546697', 'indices': [74, 97], 'media_url': 'http://pbs.twimg.com/media/Ez-IKS9VIAk0pH7.jpg', 'media_url_https': 'https://pbs.twimg.com/media/Ez-IKS9VIAk0pH7.jpg', 'url': 'https://t.co/NHtxi4tWMt', 'display_url': 'pic.twitter.com/NHtxi4tWMt', 'expanded_url': 'https://twitter.com/AmanRaj13635379/status/1386976933083115522/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'medium': {'w': 479, 'h': 811, 'resize': 'fit'}, 'small': {'w': 402, 'h': 680, 'resize': 'fit'}, 'large': {'w': 479, 'h': 811, 'resize': 'fit'}}}]}, 'extended_entities': {'media': [{'id': 1386976920722546697, 'id_str': '1386976920722546697', 'indices': [74, 97], 'media_url': 'http://pbs.twimg.com/media/Ez-IKS9VIAk0pH7.jpg', 'media_url_https': 'https://pbs.twimg.com/media/Ez-IKS9VIAk0pH7.jpg', 'url': 'https://t.co/NHtxi4tWMt', 'display_url': 'pic.twitter.com/NHtxi4tWMt', 'expanded_url': 
# 'https://twitter.com/AmanRaj13635379/status/1386976933083115522/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'medium': {'w': 479, 'h': 811, 'resize': 'fit'}, 'small': {'w': 402, 'h': 680, 'resize': 'fit'}, 'large': {'w': 479, 'h': 811, 'resize': 'fit'}}}]}, 'source': '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', 'in_reply_to_status_id': 1386874127147945984, 'in_reply_to_status_id_str': '1386874127147945984', 'in_reply_to_user_id': 1084769827271598080, 
# 'in_reply_to_user_id_str': '1084769827271598080', 'in_reply_to_screen_name': 'myogioffice', 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'lang': 'hi'}, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1382609997964537857/vj_P2XUo_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1382609997964537857/vj_P2XUo_normal.jpg', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': False, 'live_following': False, 'follow_request_sent': False, 'notifications': False, 'muting': False, 'blocking': False, 'blocked_by': False, 'translator_type': 'none', 'withheld_in_countries': []}, id=1382609657429037059, id_str='1382609657429037059', name='Aman Rajput', screen_name='AmanRaj13635379', location='', description='Aman Rajput', url=None, entities={'description': {'urls': []}}, protected=False, followers_count=8, friends_count=73, listed_count=0, created_at=datetime.datetime(2021, 4, 15, 8, 20, 19), favourites_count=5, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=1, lang=None, status=Status(_api=<tweepy.api.API object at 0x0000011912647160>, _json={'created_at': 'Tue Apr 27 09:34:04 +0000 2021', 'id': 1386976933083115522, 'id_str': '1386976933083115522', 'text': '@myogioffice @myogiadityanath Allah ham sab ko is bimari se mhefujh rakhe https://t.co/NHtxi4tWMt', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'myogioffice', 'name': 'Yogi Adityanath Office', 'id': 1084769827271598080, 'id_str': '1084769827271598080', 'indices': [0, 12]}, {'screen_name': 'myogiadityanath', 'name': 'Yogi Adityanath', 'id': 3437532637, 'id_str': '3437532637', 'indices': [13, 29]}], 'urls': [], 'media': [{'id': 1386976920722546697, 'id_str': '1386976920722546697', 'indices': [74, 97], 'media_url': 'http://pbs.twimg.com/media/Ez-IKS9VIAk0pH7.jpg', 'media_url_https': 'https://pbs.twimg.com/media/Ez-IKS9VIAk0pH7.jpg', 'url': 'https://t.co/NHtxi4tWMt', 'display_url': 'pic.twitter.com/NHtxi4tWMt', 'expanded_url': 'https://twitter.com/AmanRaj13635379/status/1386976933083115522/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'medium': {'w': 479, 'h': 811, 'resize': 'fit'}, 'small': {'w': 402, 'h': 680, 'resize': 'fit'}, 'large': {'w': 479, 'h': 811, 'resize': 'fit'}}}]}, 'extended_entities': {'media': [{'id': 1386976920722546697, 'id_str': '1386976920722546697', 'indices': [74, 97], 'media_url': 'http://pbs.twimg.com/media/Ez-IKS9VIAk0pH7.jpg', 
# 'media_url_https': 'https://pbs.twimg.com/media/Ez-IKS9VIAk0pH7.jpg', 'url': 'https://t.co/NHtxi4tWMt', 'display_url': 'pic.twitter.com/NHtxi4tWMt', 'expanded_url': 'https://twitter.com/AmanRaj13635379/status/1386976933083115522/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'medium': {'w': 479, 'h': 811, 'resize': 'fit'}, 'small': {'w': 402, 'h': 680, 'resize': 'fit'}, 'large': {'w': 479, 'h': 811, 'resize': 'fit'}}}]}, 'source': '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', 'in_reply_to_status_id': 1386874127147945984, 'in_reply_to_status_id_str': 
# '1386874127147945984', 'in_reply_to_user_id': 1084769827271598080, 'in_reply_to_user_id_str': '1084769827271598080', 'in_reply_to_screen_name': 'myogioffice', 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 
# 0, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'lang': 'hi'}, created_at=datetime.datetime(2021, 4, 27, 9, 34, 4), id=1386976933083115522, id_str='1386976933083115522', text='@myogioffice @myogiadityanath Allah ham sab ko is bimari se mhefujh rakhe https://t.co/NHtxi4tWMt', truncated=False, entities={'hashtags': [], 
# 'symbols': [], 'user_mentions': [{'screen_name': 
# 'myogioffice', 'name': 'Yogi Adityanath Office', 
# 'id': 1084769827271598080, 'id_str': '1084769827271598080', 'indices': [0, 12]}, {'screen_name': 'myogiadityanath', 'name': 'Yogi Adityanath', 'id': 3437532637, 'id_str': '3437532637', 'indices': 
# [13, 29]}], 'urls': [], 'media': [{'id': 1386976920722546697, 'id_str': '1386976920722546697', 'indices': [74, 97], 'media_url': 'http://pbs.twimg.com/media/Ez-IKS9VIAk0pH7.jpg', 'media_url_https': 'https://pbs.twimg.com/media/Ez-IKS9VIAk0pH7.jpg', 'url': 'https://t.co/NHtxi4tWMt', 'display_url': 'pic.twitter.com/NHtxi4tWMt', 'expanded_url': 'https://twitter.com/AmanRaj13635379/status/1386976933083115522/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'medium': {'w': 479, 'h': 811, 'resize': 'fit'}, 'small': {'w': 402, 'h': 680, 'resize': 'fit'}, 'large': {'w': 479, 'h': 811, 'resize': 'fit'}}}]}, extended_entities={'media': [{'id': 1386976920722546697, 'id_str': '1386976920722546697', 'indices': [74, 97], 'media_url': 'http://pbs.twimg.com/media/Ez-IKS9VIAk0pH7.jpg', 'media_url_https': 'https://pbs.twimg.com/media/Ez-IKS9VIAk0pH7.jpg', 'url': 'https://t.co/NHtxi4tWMt', 'display_url': 'pic.twitter.com/NHtxi4tWMt', 'expanded_url': 'https://twitter.com/AmanRaj13635379/status/1386976933083115522/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'medium': {'w': 479, 'h': 811, 'resize': 'fit'}, 'small': {'w': 402, 'h': 680, 'resize': 'fit'}, 'large': {'w': 479, 'h': 811, 'resize': 'fit'}}}]}, source='Twitter for Android', source_url='http://twitter.com/download/android', in_reply_to_status_id=1386874127147945984, in_reply_to_status_id_str='1386874127147945984', in_reply_to_user_id=1084769827271598080, in_reply_to_user_id_str='1084769827271598080', in_reply_to_screen_name='myogioffice', geo=None, coordinates=None, place=None, contributors=None, is_quote_status=False, retweet_count=0, favorite_count=0, favorited=False, retweeted=False, possibly_sensitive=False, lang='hi'), contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='F5F8FA', profile_background_image_url=None, profile_background_image_url_https=None, profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1382609997964537857/vj_P2XUo_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1382609997964537857/vj_P2XUo_normal.jpg', profile_link_color='1DA1F2', profile_sidebar_border_color='C0DEED', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=True, default_profile=True, default_profile_image=False, following=False, live_following=False, follow_request_sent=False, notifications=False, muting=False, blocking=False, blocked_by=False, translator_type='none', withheld_in_countries=[])



# class listener(tweepy.StreamListener):

# 	def on_data(self, status):
# 		try:
# 			# enter your code here

# 		except BaseException as e:
# 			print('failed on_status,',str(e)) # print the error code obtained from twitter
# 			time.sleep(15*60) # provide a time before resuming the code when an error arises

# 	def on_error(self, status):
# 		print(status)
