from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
mydb = client["stackoverflow"]
mydb['users'].drop()
exit()