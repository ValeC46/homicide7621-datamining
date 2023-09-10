import os
import pandas as pd

if not os.path.exists('csv'):
    os.mkdir('csv')

# From https://www.murderdata.org/p/data-docs.html
url = 'https://www.dropbox.com/s/as16jfs22env37r/SHR76_21.csv?dl=1'

data = pd.read_csv(url)

data.drop(columns=['Ori', 'Agency', 'Source', 'StateName', 'ActionType', 'Subcircum', 'FileDate', 'MSA'], inplace=True)
print(data.info())

data.to_csv('csv/rawdata.csv', index=False)