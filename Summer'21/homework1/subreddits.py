# import requests
# from dotenv import load_dotenv
# load_dotenv()
# import os
# # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
# auth = requests.auth.HTTPBasicAuth(os.getenv('REDDIT_CLIENT'), os.getenv('REDDIT_SECRET'))

# # here we pass our login method (password), username, and password
# data = {'grant_type': 'password',
#         'username': os.getenv('REDDIT_USERNAME'),
#         'password': os.getenv('REDDIT_PASSWORD')}
# # print(data)

# # setup our header info, which gives reddit a brief description of our app
# headers = {'User-Agent': 'MyBot/0.0.1'}

# # send our request for an OAuth token
# res = requests.post('https://www.reddit.com/api/v1/access_token',
#                     auth=auth, data=data, headers=headers)
# print(res.json())
# # convert response to JSON and pull access_token value
# TOKEN = res.json()['access_token']

# # add authorization to our headers dictionary
# headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# # while the token is valid (~2 hours) we just add headers=headers to our requests
# # print(requests.get('https://oauth.reddit.com/api/v1/me', headers=headers))


# res = requests.get("https://oauth.reddit.com/r/india/hot.json?limit=1000&t=year",
#                    headers=headers)

# print(res.json())



from psaw import PushshiftAPI
api = PushshiftAPI()
data = list(api.search_submissions(
    subreddit='indianfood',
    limit=1000
))
data = [thing.d_ for thing in data]
print(len(data))

import json
with open("india_indianfood.json", "w") as f:
    json.dump({
            'posts':data
    },f)
