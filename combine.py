import os
import pandas as pd
cwd = os.path.abspath('') 
files = os.listdir(cwd)  

## Method 1 gets the first sheet of a given file
df = pd.DataFrame()
for file in files:
    if file.endswith('.xls'):
        df = df.append(pd.read_excel(file), ignore_index=True) 
df.head() 
df.to_excel('air_pixabay_src.xlsx')
