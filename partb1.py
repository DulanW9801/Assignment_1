## Part B Task 1

import re
import pandas as pd
import os

filenames = os.listdir('cricket')
pattern = r'[A-Z]{4}-\d{3}[A-Z]?'
doc_id_list = []
i = 0
for i in range(len(filenames)):
    txt = open('cricket\\'+ filenames[i]).read()
    doc_id = re.search(pattern, txt)
    if doc_id != None:
        doc_id_list.append(doc_id.group())
    else:
        doc_id_list.append('Document ID not found.')
    i += 1
df = pd.DataFrame({'filename' : pd.Series(filenames), 'documentID' : pd.Series(doc_id_list)})
df.to_csv('partb1.csv', index = False)


