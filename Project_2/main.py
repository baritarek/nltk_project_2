from Project_2.subproject1 import indexer_processor
from Project_2.subproject2 import boolean_model
from Project_2.subproject3 import lossy_compression_tools, lossy_compression

PATH = 'postings_list.json'

if __name__ == "__main__":
    files = indexer_processor.process_readable_files()

    tokens = indexer_processor.tokenize(files)

    index_list = indexer_processor.create_inverted_index(tokens)

    print('inverted index', len(index_list))

    results = boolean_model.process_query()

    fold = lossy_compression_tools.case_folding(index_list)

    print('testing', len(fold))

    unwanted_numbers = lossy_compression_tools.remove_numbers(index_list)

    print('testing', len(unwanted_numbers))

    stem = lossy_compression_tools.stemming(index_list)

    print('testing', len(stem))

    testTable = lossy_compression.displayTable(PATH)
