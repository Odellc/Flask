import os
import pandas as pd
import sys
from pprint import pprint





data = pd.read_excel("C:\\Users\\codel\\Desktop\\noob.xlsx")

my_data = [] #data.to_json(orient="records")

for row in data.itertuples(index=False):
    row_data = {}

    for h, header in enumerate(data.columns):
        row_data[header] = row[h]
    
    my_data.append(row_data)

pprint(my_data)
