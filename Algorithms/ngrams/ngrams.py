from nltk import word_tokenize 
from nltk.util import ngrams


text = ['cant railway station', 'citadel hotel', 'police stn']
for line in text:
    token = word_tokenize(line)
    bigram = list(ngrams(token, 2)) 
    print(bigram)


print([[b for b in zip(l.split(" ")[:-1], l.split(" ")[1:])] for l in text])
# print([[b for b in zip(l.split(" ")[:-(n-1)], l.split(" ")[(n-1):])] for l in text])