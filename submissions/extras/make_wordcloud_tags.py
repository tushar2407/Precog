from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 
from tqdm import tqdm
from PIL import Image
import numpy as np

mask = np.array(Image.open('cloud.png'))

file = open("lis.txt", "r+")
d = eval(file.read())
d = sorted(d, key= lambda x : x[0], reverse=True)
string = ""

for ind,i in tqdm(enumerate(d)):
    word = i[1]+" "
    string+=word*i[0]
    # print(string)
    if id==100:
        break
stopwords = set(STOPWORDS) 

wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='rainbow', collocations=False, stopwords = STOPWORDS, mask=mask).generate(string)

wordcloud.to_file("tag_wordcloud.jpg")