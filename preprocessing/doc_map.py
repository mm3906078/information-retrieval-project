import pandas as pd
from tqdm import tqdm, trange
import preprocess

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

print("Reading crawled files...")
docs = pd.concat([pd.read_csv("../crawler/" + file, nrows=50) for file in tqdm(files)])["Text"].tolist()

print("Preprocessing documents...")
docs = [preprocess.preprocess(doc) for doc in tqdm(docs)]

print("Saving processed docs...")
for i in trange(len(docs)):
	with open(f'{i}.txt', 'w', encoding="utf-8") as doc_i:
		doc_i.write(str(docs[i]))
