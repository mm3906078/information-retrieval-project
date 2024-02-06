#!/usr/bin/env python3

import sys
import os
import math
import numpy as np
from tqdm import tqdm
path = os.path.abspath('../')
sys.path.append(path)
import preprocessing.preprocess as preprocess

# Definitions
Token = str
Doc_id = int
Frequency = int
Bag_of_words = dict[Token, Frequency]

# Function Definitions

def normalize(wf: Bag_of_words) -> Bag_of_words:
    norm = math.sqrt(sum(frequency ** 2 for frequency in wf.values()))
    return {term: frequency / norm for term, frequency in wf.items()}

def vectorize(query: list[Token]) -> Bag_of_words:
    bag: Bag_of_words = {}
    for token in query:
        bag[token] = bag.get(token, 0) + 1
    wf = {term: math.log1p(frequency) for term, frequency in bag.items()}
    return normalize(wf)

def cosine_score(query: Bag_of_words, doc_id: Doc_id, idx: dict[Doc_id, Bag_of_words]) -> float:
    return sum(query[term] * (idx[doc_id][term] if term in idx[doc_id] else 0) for term in query)

def Gaussian_RBF_kernel(distance: float) -> float:
    sigma = 1
    mu = 1
    return math.exp(-0.5 * ((distance - mu) / sigma) ** 2)

def tf_idf_top_doc(query: list[Token], idx: dict[Doc_id, Bag_of_words], N: int) -> tuple:
    scores = [(Gaussian_RBF_kernel(cosine_score(vectorize(query), doc_id, idx)), doc_id) for doc_id in range(N)]
    scores.sort(reverse=True)
    return scores[0]

def labse_top_doc(query: str, corpus_embeddings) -> tuple:
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer('sentence-transformers/LaBSE')
    query_embedding = model.encode(query)
    hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=1)[0]
    top_hit = hits[0]
    return (top_hit['corpus_id'], top_hit['score'])

# Main Execution
labse_input = input("Select indexing method [T = tf-idf, l = LaBSE]: ").lower()
query = preprocess.preprocess(input("Enter the query: "))
query_str = " ".join(query)  # Used for LaBSE

if labse_input in ["l", "labse"]:
    corpus_embeddings = np.load("embeddings.npy")
    top_doc_id, top_score = labse_top_doc(query_str, corpus_embeddings)
    print(f"LaBSE top doc_id = {top_doc_id} with score = {top_score:.4f}")
else:
    fidx: dict[Token, dict[Doc_id, Frequency]] = eval(open(f'fidx.txt', encoding="utf-8").read())
    idx: dict[Doc_id, Bag_of_words] = eval(open(f'idx.txt', encoding="utf-8").read())
    N = len(idx)  # Assuming N is the total number of documents
    top_score, top_doc_id = tf_idf_top_doc(query, idx, N)
    print(f"TF-IDF top doc_id = {top_doc_id} with score = {top_score:.4f}")
