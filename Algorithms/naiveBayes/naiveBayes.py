import os
root_dir = './machine-learning-101-master/chapter1/train-mails'
TRAIN_DIR = './machine-learning-101-master/chapter1/train-mails'
TEST_DIR = './machine-learning-101-master/chapter1/test-mails'
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from collections import Counter
from tqdm import tqdm

def make_dictionary(root_dir):
    all_words = []
    emails = [os.path.join(root_dir,f) for f in os.listdir(root_dir)]
    for mail in emails:
        with open(mail) as m:
            for line in m:
                words = line.split()
                all_words += words
    dictionary = Counter(all_words)

    list_to_remove = list(dictionary)
    for item in list_to_remove:
        if item.isalpha() == False:
            del dictionary[item]
        elif len(item) == 1:
            del dictionary[item]
    # consider only 3000 most common words

    dictionary = dictionary.most_common(3000)

    return dictionary

def extract_features(email_dir, dictionary):
    files = [os.path.join(email_dir, fi) for fi in os.listdir(email_dir)]
    features_matrix = np.zeros((len(files), 3000))
    train_labels = np.zeros(len(files))
    count = 0
    docID = 0
    for fil in tqdm(files):
        with open(fil) as fi:
            for i,line in enumerate(fi):
                if i==2:
                    words = line.split()
                    for word in words:
                        wordID = 0
                        for i,d in enumerate(dictionary):
                            if d[0] == word:
                                wordsID = i
                                features_matrix[docID, wordID] = words.count(word)
            train_labels[docID] = 0
            filepathTokens = fil.split('/')
            lastToken = filepathTokens[len(filepathTokens) - 1]
            if lastToken.startswith("spmsg"):
                train_labels[docID] = 1
                count += 1
            docID +=1
    return features_matrix, train_labels

dictionary = make_dictionary(TRAIN_DIR)
features_matrix, labels = extract_features(TRAIN_DIR, dictionary)
test_feature_matrix, test_labels = extract_features(TEST_DIR, dictionary)

model = GaussianNB()

model.fit(features_matrix, labels)

predicted_labels = model.predict(test_feature_matrix)

accuracy = accuracy_score(test_labels, predicted_labels)

print(accuracy, " accuracy")