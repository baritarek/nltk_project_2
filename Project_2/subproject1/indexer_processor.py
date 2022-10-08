import json
import os
from collections import OrderedDict

import nltk
from nltk import RegexpTokenizer, word_tokenize

FILES_TO_PROCESS = ['reut2-000.sgm', 'reut2-001.sgm', 'reut2-002.sgm', 'reut2-003.sgm', 'reut2-004.sgm',
                    'reut2-005.sgm',
                    'reut2-006.sgm', 'reut2-007.sgm', 'reut2-008.sgm', 'reut2-009.sgm', 'reut2-0010.sgm',
                    'reut2-0011.sgm',
                    'reut2-0012.sgm', 'reut2-0013.sgm', 'reut2-0014.sgm', 'reut2-0015.sgm', 'reut2-0016.sgm',
                    'reut2-0017.sgm', 'reut2-0018.sgm', 'reut2-0019.sgm', 'reut2-0020.sgm', 'reut2-0021.sgm']


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


class indexer_processor:
    """
    This function is used to read and clean the filenames while having a latin-1 encoded while also removing any lines
    before and after the html tags.
    @:param folder used to process the reuters21578 file directory
    @:param files_to_process will be processing the first five selected fiels
    """


"""
The function is used to tokenize each word found in the files using the ntlk.word_tokenize
@:param lines used to read the lines of the files and tokenize each word 
"""


def process_readable_files(folder='reuters21578', files_to_process=FILES_TO_PROCESS):
    # loop files directory using os.listidir()
    files = [f for f in os.listdir(folder) if f in files_to_process]
    sentences = []
    for file in files:
        get_pure_sentences = open(f'reuters21578/{file}', encoding='latin-1').read()
        tokenizer = RegexpTokenizer('\s+|<[^>]*>|&#[\d+][\S+]|;', gaps=True)
        raw = tokenizer.tokenize(get_pure_sentences)
        sentences.append(' '.join(raw))

    return sentences


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


def create_inverted_index(docs):
    inverted_index = {}
    for docID, doc in enumerate(docs):
        for term in doc:
            if term in inverted_index:
                inverted_index[term].add(docID)
            else:
                inverted_index[term] = {docID}

    inverted_index = OrderedDict(sorted(inverted_index.items()))

    raw = json.dumps(inverted_index, cls=SetEncoder)

    with open('postings_list.json', 'w') as fp:
        fp.write(str(raw))

    return inverted_index


def sort(index_list):
    return OrderedDict(sorted(index_list.items()))
