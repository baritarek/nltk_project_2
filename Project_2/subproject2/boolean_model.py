import json

from Project_2.subproject1 import indexer_processor
from Project_2.subproject1.indexer_processor import indexer_processor

"""
Will ask user to input the query term they are searching 
@:return the query term
"""
def get_query():
    query = input('Type your query: ')
    query = query.strip()
    return query


"""
Retrieve the query term and read the posting file while returing the query found with index in .json file 
@:return dict() of query term
"""
def process_query():
    query = get_query()
    dictionary = dict()
    # read the posting list terms
    with open("postings_list.json", 'r') as json_file:
        dictionary = json.load(json_file)

    # create query file of resutls in dictionary
    with open("querySamples.json", 'a', encoding='utf-8') as outputFile:
        if query not in dictionary:
            print("Term not found!")
            exit()
        # dump the term found in json
        json.dump({query: dictionary[query]}, outputFile, indent=3)
        outputFile.write(',')
    return dictionary[query]
