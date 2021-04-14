## Part B Task 4
import re
import pandas as pd
import os
import sys
import nltk
from nltk.stem import PorterStemmer
porter = PorterStemmer()

def stem_words(word_list):
    stem_lst = []
    for word in word_list:
        stem_lst.append(porter.stem(word))
    return(stem_lst)


def preprocessing(filename):
    file0 = open(filename).read()
    file1 = re.sub(r'[^A-Za-z]+', ' ',file0)
    file2 = re.sub(r'\s+', ' ',file1)
    file3 = file2.lower()
    return(file3)

df = pd.read_csv('partb1.csv')
os.chdir(r'cricket')
i = 0
j = 0
doc_id = []
for i in range(1,len(sys.argv)):
    keyword = sys.argv[i]
    for j  in range(124):
        processed_file = preprocessing(df.filename[j])
        word_list = nltk.word_tokenize(processed_file)
        stem_list = stem_words(word_list)
        if (porter.stem(keyword.lower()) in stem_list and df.documentID[j] not in doc_id):
            doc_id.append(df.documentID[j])
        j += 1
    i += 1
print(doc_id)