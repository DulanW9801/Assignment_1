## Part B Task 5
import re
import os
import sys
import pandas as pd
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
porter = PorterStemmer()

def stem_string(processed_file):
    token_words=word_tokenize(processed_file)
    stem_string=[]
    for word in token_words:
        stem_string.append(porter.stem(word))
        stem_string.append(" ")
    return "".join(stem_string)


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
keyword_count = []
for i in range(1,len(sys.argv)):
    for j in range(124):
        temp = []
        processed_file = preprocessing(df.filename[j])
        string = stem_string(processed_file)
        count = re.findall(sys.argv[i], string)
        print(string)
        j += 1
    i += 1

        
        

    
