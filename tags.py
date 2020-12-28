import pymongo
from tqdm import tqdm
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["stackoverflow"]
mycol = mydb["tags"]

dic = {}
# print(mycol.find_one().keys())
for i in tqdm(mycol.find()):
    # print(i)
    dic[i['Tagname']] = int(i['Count'])


# file = open("dic.txt", "w+")
# file.write(str(dic))
# file.close()

lis = []
for i in dic.keys():
    lis.append((dic[i],i))

# file = open("lis.txt", "w+")
# file.write(str(lis))
# file.close()

lis_sorted = sorted(lis, key= lambda x : x[0], reverse=True)

print(lis_sorted[:10])