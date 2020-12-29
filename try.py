import pandas as pd

from csv import reader
from tqdm import tqdm
data = []
with open('ua.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in tqdm(csv_reader):
        data.append(row)
df = pd.DataFrame(data, columns = ['CreatedAt', 'tweets', 'User_ID', 'User_Name'])
df.to_csv('df.csv', index=False)