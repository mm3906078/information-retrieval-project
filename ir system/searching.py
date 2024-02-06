import math
import numpy as np
from tqdm import tqdm, trange
from indexing import normalize, N, Doc_id, Token, Term, Frequency, Bag_of_words
from preprocessing import preprocess
labse = input("Select indexing method [T = tf-idf, l = LaBSE]: ") in ["l", "L", "LaBSE", "labse", "LABSE"]
if labse:
	corpus_embeddings = np.load("embeddings.npy")
else:
	fidx: dict[Token, dict[Doc_id, Frequency]] = eval(open(f'fidx.txt', encoding="utf-8").read())
	idx: dict[Doc_id, Bag_of_words] = eval(open(f'idx.txt', encoding="utf-8").read())


def vectorize(query: list[Token]):
	bag: Bag_of_words = {}
	for token in query:
		if token not in bag:
			bag[token] = 1
		else:
			bag[token] += 1
	wf = {term: math.log1p(frequency) for term, frequency in bag.items()}
	return normalize(wf)


def cosine_score(query: Bag_of_words, doc_id: Doc_id):
	return sum(query[term] * (idx[doc_id][term] if term in idx[doc_id] else 0) for term in query)


def Jaccard_score(query: Bag_of_words, doc_id: Doc_id):
	q = set(query.keys())
	d = set(idx[doc_id].keys())
	return len(q & d) / len(q | d)


def F_score(query: Bag_of_words, doc_id: Doc_id):
	q = set(query.keys())
	d = set(idx[doc_id].keys())
	return 2 * len(q & d) / (len(d) + len(q))


def Gaussian_RBF_kernel(distance: float):
	sigma = 1
	mu = 1
	return math.exp(-0.5 * ((distance - mu) / sigma) ** 2)  # /(2*math.pi*sigma**2)**0.5


query = preprocess.preprocess(input("Enter the query: "))

if not labse:
	method = input("Enter scoring method [f = F-score, C = cosine, j = jaccard]: ")
	score = cosine_score
	if method == 'f':
		score = F_score
	if method == 'j':
		score = Jaccard_score
	scores = [(Gaussian_RBF_kernel(score(vectorize(query), doc_id)), doc_id) for doc_id in trange(N)]
	scores.sort(reverse=True)
	print(f"doc_id = {scores[0][1]} with score = {scores[0][0]}")
else:
	from sentence_transformers import SentenceTransformer, util
	model = SentenceTransformer('sentence-transformers/LaBSE')
	query_embedding = model.encode(query)
	hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=5)[0]
	for hit in hits:
		print(hit['corpus_id'], "(Score: {:.4f})".format(hit['score']))
