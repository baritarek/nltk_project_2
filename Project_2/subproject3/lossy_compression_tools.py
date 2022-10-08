import math

import nltk.corpus
from nltk.stem import PorterStemmer
from tqdm import tqdm
from os import path


def frequency(dictionary):
    val = 0
    for keys in dictionary.keys():
        val += dictionary[keys][0]
    return val


def stemming(dictionary):
    porter_stemmer = PorterStemmer()
    stemming_dict = dict()

    for key in dictionary.keys():
        stemming_dict[porter_stemmer.stem(key)] = dictionary[key]

    return stemming_dict


def remove_stopwords(dictionary, num_words):
    stopwords = nltk.corpus.stopwords.words('english')

    if num_words == 30:
        for words in stopwords[:num_words]:
            if words.lower() in dictionary:
                del dictionary[words.lower()]
    else:
        for words in stopwords[30:num_words]:
            if words.lower() in dictionary:
                del dictionary[words.lower()]

    return dictionary


def case_folding(dictionary):
    dict_lower = {k.lower(): v for k, v in dictionary.items()}
    return dict_lower


def remove_numbers(dictionary):
    for key in list(dictionary.keys()):
        val = key.replace(",", "")
        if isDigit(val):
            del dictionary[key]

    return dictionary


def delta(prev, new):
    return math.floor(((prev - new) / prev) * 100)


def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
