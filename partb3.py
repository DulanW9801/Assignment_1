## Part B Task 3
import re
import sys
import pandas as pd
import nltk
import os

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
        if (keyword.lower() in word_list and df.documentID[j] not in doc_id):
            doc_id.append(df.documentID[j])
        j += 1
    i += 1
print(doc_id)

            



