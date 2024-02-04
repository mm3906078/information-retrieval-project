def prepreprocess4(data):
    # normalizing data
    normalizer = Normalizer()
    norm_data = normalizer.remove_specials_chars(data)
    norm_data = normalizer.normalize(norm_data)
    # Tokenize data
    tokens = word_tokenize(norm_data)

    # Remove stopwords and punctuation
    stop_words = set(stopwords_list())
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatize words
    lemmatizer = Lemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens


def preprocess3(data):
    # normalizing data
    normalizer = Normalizer()
    norm_data = normalizer.remove_specials_chars(data)
    norm_data = normalizer.normalize(norm_data)
    # Tokenize data
    tokens = word_tokenize(norm_data)

    # Lemmatize words
    lemmatizer = Lemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens


def prepreprocess2(data):
    # normalizing data
    normalizer = Normalizer()
    norm_data = normalizer.remove_specials_chars(data)
    norm_data = normalizer.normalize(norm_data)
    # Tokenize data
    tokens = word_tokenize(norm_data)

    # Remove stopwords and punctuation
    stop_words = set(stopwords_list())
    tokens = [word for word in tokens if word not in stop_words]

    return tokens


def prepreprocess1(data):
    # normalizing data
    normalizer = Normalizer()
    norm_data = normalizer.remove_specials_chars(data)
    norm_data = normalizer.normalize(norm_data)
    # Tokenize data
    tokens = word_tokenize(norm_data)

    return tokens
