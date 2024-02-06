#!/usr/bin/env python3

import pandas as pd
from tqdm import tqdm, trange
import preprocess
import os

files = [
    'hamshahri/culture.csv',
    'hamshahri/economy.csv',
    'hamshahri/politics.csv',
    'hamshahri/sport.csv',
    'irna/culture.csv',
    'irna/economy.csv',
    'irna/politics.csv',
    'irna/sport.csv',
    'isna/culture.csv',
    'isna/economy.csv',
    'isna/politics.csv',
    'isna/sport.csv',
    'mehrnews/culture.csv',
    'mehrnews/economy.csv',
    'mehrnews/politics.csv',
    'mehrnews/sport.csv'
]

doc_category_map = []  # List to store the mapping of doc ID to category

print("Reading crawled files...")
docs = []
for file in tqdm(files):
    category = file.split('/')[1].split('.')[0]  # Extract category from the file name
    df = pd.read_csv("../crawler/" + file, nrows=50)
    for index, row in df.iterrows():
        docs.append(row["Text"])
        doc_category_map.append((len(docs) - 1, category))  # Map current doc ID to its category

print("Preprocessing documents...")
docs = [preprocess.preprocess(doc) for doc in tqdm(docs)]

# Check folder exist or create it
if not os.path.exists('docs'):
    os.makedirs('docs')

print("Saving processed docs...")
for i in trange(len(docs)):
    with open(f'docs/{i}.txt', 'w', encoding="utf-8") as doc_i:
        doc_i.write(str(docs[i]))

# Save the doc ID to category mapping to a CSV file
df_map = pd.DataFrame(doc_category_map, columns=['DocID', 'Category'])
df_map.to_csv('doc_category_map.csv', index=False)

print("Document-category mapping saved to doc_category_map.csv.")
