from pymongo import MongoClient
from tqdm import tqdm
import xml.etree.ElementTree as ET

client = MongoClient("mongodb://localhost:27017/")

mydb = client["stackoverflow"]

# doing tags
"""
mycol = mydb["tags"]
tree = ET.parse('stackoverflow.com/Tags.xml')
stud = tree.findall('row')
print(type(stud))
print(len(stud))
# print(s)
for i in stud:
    Id = i.attrib['Id']
    Tagname = i.attrib['TagName']
    Count = i.attrib['Count']
    try:
        ExcerptPostId = i.attrib['ExcerptPostId']
    except:
        ExcerptPostId = "-1"
    try:
        WikiPostId = i.attrib['WikiPostId']
    except:
        WikiPostId = "-1"
    x = {
        "Id": Id,
        "Tagname": Tagname,
        "Count": Count,
        "ExcerptPostId": ExcerptPostId,
        "WikiPostId": WikiPostId  
    }
    mycol.insert_one(x)
    print(x['Id'])
"""

#doing users
mycol = mydb['users']
tree = ET.parse('stackoverflow.com/Users.xml')
stud = tree.findall('row')
print(len(stud))
for i in tqdm(stud):
    Id = i.attrib['Id']
    Reputation = i.attrib['Reputation']
    CreationDate = i.attrib['CreationDate']
    DisplayName = i.attrib['DisplayName']
    LastAccessDate = i.attrib['LastAccessDate']
    try:
        WebsiteUrl = i.attrib['WebsiteUrl']
    except:
        WebsiteUrl = "https://localhost"
    try:
        Location = i.attrib['Location']
    except:
        Location = "Earth"
    try:
        AboutMe = i.attrib['AboutMe']
    except:
        AboutMe = ""
    Views = i.attrib['Views']
    UpVotes = i.attrib['UpVotes']
    DownVotes = i.attrib['DownVotes']
    # ProfileImageUrl = i.attrib['ProfileImageUrl']
    AccountId = i.attrib['AccountId']
    x = {
        'Id': Id,
        'Reputation': Reputation,
        'CreationDate': CreationDate,
        'DisplayName': DisplayName,
        'LastAccessDate': LastAccessDate,
        'WebsiteUrl': WebsiteUrl,
        'Location': Location,
        'AboutMe': AboutMe,
        'Views': Views,
        'UpVotes': UpVotes,
        'DownVotes': DownVotes,
        # 'ProfileImageUrl': ProfileImageUrl,
        'AccountId': AccountId
    }
    mycol.insert_one(x)
    # print(x['Id'])
"""
{
    'Id': '1', 
    'Reputation': '58679', 
    'CreationDate': '2008-07-31T14:22:31.287', 
    'DisplayName': 'Jeff Atwood', 
    'LastAccessDate': '2020-02-26T23:04:34.223', 
    'WebsiteUrl': 'http://www.codinghorror.com/blog/', 
    'Location': 'El Cerrito, CA', 
    'AboutMe': '<p><a href="http://www.codinghorror.com/blog/archives/001169.html" rel="nofollow">Stack Overflow Valued Associate #00001</a></p>\n\n<p>Wondering how our software development process works? <a href="http://www.youtube.com/watch?v=08xQLGWTSag" rel="nofollow">Take a look!</a></p>\n\n<p>Find me <a href="http://twitter.com/codinghorror" rel="nofollow">on twitter</a>, or <a href="http://www.codinghorror.com/blog" rel="nofollow">read my blog</a>. Don\'t say I didn\'t warn you <em>because I totally did</em>.</p>\n\n<p>However, <a href="http://www.codinghorror.com/blog/2012/02/farewell-stack-exchange.html" rel="nofollow">I no longer work at Stack Exchange, Inc</a>. I\'ll miss you all. Well, <em>some</em> of you, anyway. :)</p>\n', 
    'Views': '532726', 
    'UpVotes': '3378', 
    'DownVotes': '1311', 
    'ProfileImageUrl': 'https://www.gravatar.com/avatar/51d623f33f8b83095db84ff35e15dbe8?s=128&amp;d=identicon&amp;r=PG', 
    'AccountId': '1'}
"""