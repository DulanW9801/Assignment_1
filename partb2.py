# Part B Task 2
import re
import os
import sys
os.chdir(r'cricket')
pattern = r'cricket\d{3}\.txt'

def preprocessing(filename):
    file0 = open(filename).read()
    file1 = re.sub(r'[^A-Za-z]+', ' ',file0)
    file2 = re.sub(r'\s+', ' ',file1)
    file3 = file2.lower()
    return(file3)

def main(txt_file):
    output = preprocessing(txt_file)
    return(print(output))

if(re.search(pattern, sys.argv[1])):
    txt_file = re.split(r'cricket', sys.argv[1])[1]
    if txt_file not in os.listdir():
        print('Invalid Input!')
    else:
        main(txt_file)
else:
    print('Invalid Input!')
