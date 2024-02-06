characters_to_remove = [':', ';', '""', '!', '؟', '|', '>', '<', '،', "''", ')', '(', '»', '«', '_', '-', '؛', '.',
                        '\u200c', '\\u200c', '/u200c', '//u200c', 'u200c\\', '/', '\\', 'انتهای پیام', 'کد خبر',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
remove_stopwords = input("Do you want to remove stopwords? [y, N] ") in ["YES", "Yes", "Y", "yes", "y"]
lemmatize = input("Do you want to lemmatize words? [y, N] ") in ["YES", "Yes", "Y", "yes", "y"]
from hazm import Lemmatizer, Normalizer, word_tokenize, stopwords_list
normalizer = Normalizer()
lemmatizer = Lemmatizer()


def preprocess(doc):
    # Removing bad characters
    for char in characters_to_remove:
        doc = doc.replace(char, " ")

    # normalizing doc
    norm_doc = normalizer.remove_specials_chars(doc)
    norm_doc = normalizer.normalize(norm_doc)

    # Tokenize doc
    tokens = word_tokenize(norm_doc)

    # Remove stopwords
    if remove_stopwords:
        stop_words = set(stopwords_list())
        tokens = [word for word in tokens if word not in stop_words]

    # Lemmatize words
    if lemmatize:
        tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens
