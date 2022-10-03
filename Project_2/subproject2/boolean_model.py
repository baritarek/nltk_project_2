import os

PATH = "output/sampleQueries.json"


def queryProcessor(query):
    query_term = query[0].replace(" ", "")
    dictionary = dict()

    assert type(dictionary) == dict

    if query_term not in dictionary:
        exit()

    output = {query_term: dictionary[query_term]}

    return output
# json.dump(output, outputFile, indent=3)
