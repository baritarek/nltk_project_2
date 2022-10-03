import os
from collections import OrderedDict

import nltk
from nltk import RegexpTokenizer, word_tokenize

files_to_process = ['reut2-000.sgm', 'reut2-001.sgm', 'reut2-002.sgm', 'reut2-003.sgm', 'reut2-004.sgm']


class IndexProcessor():
    """
    This function is used to read and clean the filenames while having a latin-1 encoded while also removing any lines
    before and after the html tags.
    @:param folder used to process the reuters21578 file directory
    @:param files_to_process will be processing the first five selected fiels
    """


def process_readable_files(folder='reuters21578', files_to_process=files_to_process):
    # loop files directory using os.listidir()
    files = [f for f in os.listdir(folder) if f in files_to_process]
    sentences = []
    for file in files:
        get_pure_sentences = open(f'reuters21578/{file}', encoding='latin-1').read()
        tokenizer = RegexpTokenizer('\s+|<[^>]*>|&#[\d+][\S+]|;', gaps=True)
        raw = tokenizer.tokenize(get_pure_sentences)
        sentences.append(' '.join(raw))

    return sentences


"""
The function is used to tokenize each word found in the files using the ntlk.word_tokenize
@:param lines used to read the lines of the files and tokenize each word 
"""


def tokenize(raw_text_files):
    tokens = []

    for i, file in enumerate(raw_text_files):
        document = word_tokenize(file)
        tokens.append(document)

    return tokens


"""Create a inverted index of words (tokens or terms) from a list of terms

    Parameters:
    words (list of str): tokenized document text

    Returns:
    Inverted index of document (dict)

   """


def inverted_index(docs):
    inverted_index = {}

    for docID, doc in enumerate(docs):
        for term in doc:
            if term in inverted_index:
                inverted_index[term].add(docID)
            else:
                inverted_index[term] = {docID}

    inverted_index = sort(inverted_index)
    return inverted_index


"""Insert document id into Inverted Index

   Parameters:
   inverted (dict): Inverted Index
   doc_id (int): Id of document been added
   doc_index (dict): Inverted Index of a specific document.

   Returns:
   Inverted index of document (dict)

  """


def sort(index_list):
    return OrderedDict(sorted(index_list.items()))
