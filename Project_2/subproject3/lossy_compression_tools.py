import math, json
from nltk.stem import PorterStemmer
from tqdm import tqdm
from os import path


def frequency(dictionary):
    val = 0
    for keys in dictionary.keys():
        val += dictionary[keys][0]
    return val


def stemming(dictionary):
    ps = PorterStemmer()
    stemming_dict = dict()
    for keys in dictionary.keys():
        if ps.stem(keys) not in stemming_dict:
            stemming_dict[ps.stem(keys)] = dictionary[keys]
        else:
            stemming_dict[ps.stem(keys)][1] = sorted(set(stemming_dict[ps.stem(keys)][1] + dictionary[keys][1]))
            stemming_dict[ps.stem(keys)][0] = len(stemming_dict[ps.stem(keys)][1])

    return stemming_dict


def remove_stopwords(dictionary, num_words):
    stopwords = []
    assert path.exists("utilities/stopwords.txt"), "Make sure the utilities package contains the stopwords!"
    with open("utilities/stopwords.txt", 'r') as fp:
        stopwords = fp.readlines()

    stopwords = [words.replace('\n', "") for words in stopwords]

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
    case_folding_dict = dict()
    print("\n")
    for keys in tqdm(dictionary.keys()):
        if keys.lower() not in case_folding_dict:
            case_folding_dict[keys.lower()] = dictionary[keys]
        else:
            case_folding_dict[keys.lower()][1] = sorted(set(case_folding_dict[keys.lower()][1] + dictionary[keys][1]))
            case_folding_dict[keys.lower()][0] = len(case_folding_dict[keys.lower()][1])

    return case_folding_dict


def remove_numbers(dictionary):
    for key in list(dictionary.keys()):
        if key.isdigit():
            del dictionary[key]

    return dictionary


def delta(prev, new):
    return math.floor(((prev - new) / prev) * 100)
