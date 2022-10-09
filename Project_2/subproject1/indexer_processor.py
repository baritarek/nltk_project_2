import json
import os
from collections import OrderedDict
from nltk import RegexpTokenizer, word_tokenize

"""
The following class is created in order to encode instances of a data type as a JSON object
"""


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        # if instance of the object return json
        if isinstance(obj, set):
            return list(obj)
        # if not encode it to json
        return json.JSONEncoder.default(self, obj)


"""
The following class will be used to develop a module that will process reuters21578 documents , accpet a list as tokens
and output the terms while removing duplcated. Moreover, it will also sort the files and create a posting list of terms 
in JSON format
"""


class indexer_processor:
    """
This function is used to read and clean the filenames while having a latin-1 encoded while also removing any lines
before and after the html tags.
@:param folder used to process the reuters21578 file directory
@:param files_to_process will be processing the first five selected fiels
@:return the pure sentences after removing the tags
"""


def process_readable_files(folder='reuters21578'):
    # loop files directory using os.listidir()
    files = [f for f in os.listdir(folder) if f.endswith('.sgm')]
    sentences = []
    for file in files:
        get_pure_sentences = open(f'reuters21578/{file}', encoding='latin-1').read()
        tokenizer = RegexpTokenizer('\s+|<[^>]*>|&#[\d+][\S+]|;', gaps=True)
        raw = tokenizer.tokenize(get_pure_sentences)
        sentences.append(' '.join(raw))

    return sentences


"""
Tokenize the words in Reuteurs21578
@:return a list of tokenized words from reutuers21578
"""


def tokenize(raw_text_files):
    tokens = []
    for i, file in enumerate(raw_text_files):
        document = word_tokenize(file)
        tokens.append(document)

    return tokens


"""
Create a inverted index of words (tokens or terms) from a list of terms
@:param docs (list of str): tokenized document text
@:return inverted index of sorted  documents
"""


def create_inverted_index(docs):
    inverted_index = {}
    for docID, doc in enumerate(docs):
        for term in doc:
            if term in inverted_index:
                inverted_index[term].add(docID)
            else:
                inverted_index[term] = {docID}

    # sort the inverted index terms
    inverted_index = OrderedDict(sorted(inverted_index.items()))

    # create json file that will input the inverted index values
    raw = json.dumps(inverted_index, cls=SetEncoder)

    # create posting files of invereted index to be stored
    with open('postings_list.json', 'w') as file_handler:
        file_handler.write(str(raw))

    return inverted_index


"""
Sort the terms of the inverted index found
@:param inputs the index terms in the list 
@:return a sorted inverted index posting 
"""


def sort(index_list):
    return OrderedDict(sorted(index_list.items()))
