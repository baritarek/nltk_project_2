import json

from Project_2.subproject1 import indexer_processor
from Project_2.subproject1.indexer_processor import indexer_processor


def get_query():
    query = input('Type your query: ')
    query = query.strip()
    return query


def process_query():
    query = get_query()
    dictionary = dict()
    with open("postings_list.json", 'r') as json_file:
        dictionary = json.load(json_file)

    with open("querySamples.json", 'a', encoding='utf-8') as outputFile:
        if query not in dictionary:
            print("Term not found!")
            exit()
        json.dump({query: dictionary[query]}, outputFile, indent=3)
        outputFile.write(',')
    return dictionary[query]
