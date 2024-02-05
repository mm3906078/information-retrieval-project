def preprocess4(data):
    #normalizing data
    normalizer = Normalizer()
    norm_data = normalizer.normalize(data)
    # Tokenize data
    tokens = word_tokenize(norm_data)

    # Remove stopwords and punctuation
    stop_words = set(stopwords_list())
    tokens = [word for word in tokens if word not in stop_words ]

    # Lemmatize words
    lemmatizer = Lemmatizer()
    lemma_data = str()
    for i in tokens:
        temp = lemmatizer.lemmatize(i)
        temp += ' '
        lemma_data += temp

    return lemma_data


def preprocess3(data):
    #normalizing data
    normalizer = Normalizer()
    norm_data = normalizer.normalize(data)
    # Tokenize data
    tokens = word_tokenize(norm_data)

    # Lemmatize words
    lemmatizer = Lemmatizer()
    lemma_data = str()
    for i in tokens:
        temp = lemmatizer.lemmatize(i)
        temp += ' '
        lemma_data += temp

    return lemma_data


def preprocess2(data):
    #normalizing data
    normalizer = Normalizer()
    norm_data = normalizer.normalize(data)
    # Tokenize data
    tokens = word_tokenize(norm_data)

    # Remove stopwords and punctuation
    stop_words = set(stopwords_list())
    tokens = [word for word in tokens if word not in stop_words ]

    normalized_data = str()
    for i in tokens:
        temp = i
        temp += ' '
        normalized_data += temp

    return normalized_data


def preprocess1(data):
    #normalizing data
    normalizer = Normalizer()
    norm_data = normalizer.normalize(data)


    return norm_data