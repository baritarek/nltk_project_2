import time

from IPython.core.display_functions import display

from Project_2.subproject1 import indexer_processor
from Project_2.subproject2 import boolean_model
import pprint
from Project_2.subproject3 import lossy_compression_tools, lossy_compression
import pandas as pd

PATH = 'postings_list.json'

if __name__ == "__main__":
    start = time.time()
    print('Start of Time:', start)
    files = indexer_processor.process_readable_files()

    tokens = indexer_processor.tokenize(files)

    index_list = indexer_processor.create_inverted_index(tokens)

    results = boolean_model.process_query()

    fold = lossy_compression_tools.case_folding(index_list)

    print('Case Folding: ', len(fold))

    unwanted_numbers = lossy_compression_tools.remove_numbers(index_list)

    print('Remove numbers: ', len(unwanted_numbers))

    stem = lossy_compression_tools.stemming(index_list)

    print('Stemming: ', len(stem))

    table = lossy_compression.display_table(PATH)
    end = time.time()
    print('End Time ', end)
    difference = end - start
    print('Total Time: ', difference)
