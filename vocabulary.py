import numpy as np
from hazm import *
import pandas as pd
from collections import Counter


# add other Excel files
df1 = pd.read_csv('ham_culture.csv', nrows=50)
df2 = pd.read_csv('ham_economy.csv', nrows=50)
df3 = pd.read_csv('ham_politics.csv', nrows=50)
df4 = pd.read_csv('ham_sport.csv', nrows=50)
df5 = pd.read_csv('irna_culture.csv', nrows=50)
df6 = pd.read_csv('irna_economy.csv', nrows=50)
df7 = pd.read_csv('irna_politics.csv', nrows=50)
df8 = pd.read_csv('irna_sport.csv', nrows=50)
df9 = pd.read_csv('isna_culture.csv', nrows=50)
df10 = pd.read_csv('isna_economy.csv', nrows=50)
df11 = pd.read_csv('isna_politics.csv', nrows=50)
df12 = pd.read_csv('isna_sport.csv', nrows=50)
df13 = pd.read_csv('mehr_culture.csv', nrows=50)
df14 = pd.read_csv('mehr_economy.csv', nrows=50)
df15 = pd.read_csv('mehr_politics.csv', nrows=50)
df16 = pd.read_csv('mehr_sport.csv', nrows=50)
docs = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16]

# all docs as one string for easier vocabulary creation
unprocessed = str()
for i in range(16):
    for j in range(len(docs[i])):
        unprocessed += docs[i]['Text'][j]
print(len(unprocessed))
print(type(unprocessed[0]))

# removing punctuation marks
characters_to_remove = [':', ';', '""', '!', '؟', '|', '>', '<', '.', '،', "''", ')', '(', '»', '«', '/', '\\', '_', '-', '؛',
                        '\u200c', '\u200c185', '\u200c158', '\u200c251', 'u200c\\', '\\u200c', 'انتهای پیام', 'کد خبر',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
for j in characters_to_remove:
    unprocessed = unprocessed.replace(j, '')
print(len(unprocessed))


# one of the preprocessing functions
def preprocess(data):
    # normalizing data
    normalizer = Normalizer()
    norm_data = normalizer.remove_specials_chars(data)
    norm_data = normalizer.normalize(norm_data)
    # Tokenize data
    tokens = word_tokenize(norm_data)

    # Remove stopwords
    stop_words = set(stopwords_list())
    tokens = [word for word in tokens if word not in stop_words ]

    # Lemmatize words
    lemmatizer = Lemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens


# creating tokens and vocabulary
tokens_a = preprocess(unprocessed)
count = Counter(tokens_a)
with open('vocabulary.txt', 'w', encoding="utf-8") as data:
    data.write(str(count))
