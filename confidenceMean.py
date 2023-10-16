import pandas as pd
import sys
import os
import string

filepath = sys.argv[1]

#### function to get file name

def filename (path):
    filename = os.path.basename(path)
    filename = filename.split('.', 1)
    return str(filename[0])

#### function to read in csv and output mean to confidence.csv

def confmean (path):
    dfinput = pd.read_csv(path, skiprows = 9, sep = '\t')
    confidence = dfinput.filter(['Confidence'], axis = 1)
    mean = confidence['Confidence'].mean()
    data = {
        'File': [filename(path)],
        'Mean': [mean]
    }
    df = pd.DataFrame(data)
    df.to_csv('confidence.csv', mode = 'a', index = False, header = False)

### try file path

if os.path.exists(filepath):
    print ('Report Found: ' + filename(filepath))
    confmean(filepath)
    print('confidence.csv appended succesfully.')

else: print('File Not Found!')