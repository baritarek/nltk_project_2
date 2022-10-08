import math

import nltk.corpus
from nltk.stem import PorterStemmer
from tqdm import tqdm
from os import path

"""
@:param dictionary of each term that will compute the frquency of each term
@:return the number of times each term
"""


def frequency(dictionary):
    val = 0
    for keys in dictionary.keys():
        val += dictionary[keys][0]
    return val


"""
Stem the terms with the use of porter stemmer in nltk package 
@:return stemmed terms
"""


def stemming(dictionary):
    porter_stemmer = PorterStemmer()
    stemming_dict = dict()

    for key in dictionary.keys():
        stemming_dict[porter_stemmer.stem(key)] = dictionary[key]

    return stemming_dict


"""
This function is used to remove a list of stop words from the dictionary and indicated if you want to remove 30 or 150
@:param dictionary will the terms 
@:param nums_words indicate either want 30 to 150 stopwords
"""


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


"""
Reducing all letters to lower case
@:param dictionary of terms
@:return the terms to lower case
"""


def case_folding(dictionary):
    dict_lower = {k.lower(): v for k, v in dictionary.items()}
    return dict_lower


"""
Remove all numbers in the ternms
@:param dictionary of terms
@:return the terms without any numbers
"""


def remove_numbers(dictionary):
    for key in list(dictionary.keys()):
        val = key.replace(",", "")
        if isDigit(val):
            del dictionary[key]

    return dictionary


"""
Calculate the percentage of change 
@:param prev used to calculate before
@:param new used to calcuate now 
@:return the difference of prev & new in percentage format 
"""


def delta(prev, new):
    return math.floor(((prev - new) / prev) * 100)


"""
Verify if the terms in the dictionary is a digit of either integers or floats 
"""
def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
