import math
import numpy as np
from tqdm import tqdm, trange
N = 800
Doc_id = int
Token = str
Term = str
Frequency = int
Bag_of_words = dict[Token, float]
fidx: dict[Token, dict[Doc_id, Frequency]] = {}
idx: dict[Doc_id, Bag_of_words] = {}


def add(token: Token, doc_id: Doc_id):
	if token not in fidx:
		fidx[token] = {}
	if doc_id not in fidx[token]:
		fidx[token][doc_id] = 0
	fidx[token][doc_id] += 1


def cf(term: Token):
	return sum(fidx[term].values())


def df(term: Token):
	return len(fidx[term])


def idf(term):
	return math.log(N / df(term))


def idf_smoothed(term):
	return math.log(N / (df(term) + 1)) + 1


def tf(term: Token, doc_id: Doc_id):
	return fidx[term][doc_id]


def wf(term: Token, doc_id: Doc_id):
	return math.log1p(tf(term, doc_id))


def bf(term: Token, doc_id: Doc_id):
	return bool(tf(term, doc_id))


def index():
	for term, bag_of_docs in tqdm(fidx.items()):
		for doc_id in bag_of_docs:
			if doc_id not in idx:
				idx[doc_id] = {}
			idx[doc_id][term] = wf(term, doc_id) * idf_smoothed(term)


def normalize(bag: Bag_of_words) -> Bag_of_words:
	norm = sum(x**2 for x in bag.values()) ** 0.5
	bag = {term: weighted_frequency / norm for term, weighted_frequency in bag.items()}
	return bag


def normalize_index():
	for doc_id in tqdm(idx):
		idx[doc_id] = normalize(idx[doc_id])


if __name__ == "__main__":
	print("Reading processed documents...")
 	corpus = [eval(open(f'../preprocessing/docs/{i}.txt', encoding="utf-8").read()) for i in trange(N)]
	if input("Select indexing method [T = tf-idf, l = LaBSE]: ") in ["l", "L", "LaBSE", "labse", "LABSE"]:
		from sentence_transformers import SentenceTransformer

		model = SentenceTransformer('sentence-transformers/LaBSE')
		corpus_embeddings = model.encode(corpus)
		np.save("embeddings.npy", corpus_embeddings)
	else:
		biword = input("Do you want to index biwords? [y, N] ") in ["YES", "Yes", "Y", "yes", "y"]
		print("Indexing...")
		for doc_id in trange(len(corpus)):
			if not biword:
				for token in corpus[doc_id]:
					add(token, doc_id)
			else:
				for token_id in range(len(corpus[doc_id]) - 1):
					token = corpus[doc_id][token_id] + " " + corpus[doc_id][token_id + 1]
					add(token, doc_id)

		print("Embedding...")
		print("Calculating tf-idf measurement...")
		index()

		print("Performing cosine normalization...")
		normalize_index()

		print("Saving index...")
		with open(f'fidx.txt', 'w', encoding="utf-8") as file:
			file.write(str(fidx))
		with open(f'idx.txt', 'w', encoding="utf-8") as file:
			file.write(str(idx))
