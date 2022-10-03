import math
import lossy_compression_tools
from nltk.stem import PorterStemmer


def computeTermLossy(path):
    dictionary = dict()
    results = dict()

    with open(path, 'r') as file_handler:
        dictionary = file_handler.read()

    results["unfiltered"] = len(dictionary)

    dictionary = lossy_compression_tools.remove_numbers(dictionary)
    results["no_number"] = len(dictionary)

    dictionary = lossy_compression_tools.case_folding(dictionary)
    results["case_folding"] = len(dictionary)

    dictionary = lossy_compression_tools.remove_stopwords(dictionary, 30)
    results["30_stopwords"] = len(dictionary)

    dictionary = lossy_compression_tools.remove_stopwords(dictionary, 150)
    results["150_stopwords"] = len(dictionary)

    dictionary = lossy_compression_tools.stemming(dictionary)
    results["stemming"] = len(dictionary)

    return results


def computeNonPopLossy(path):
    dictionary = dict()
    results = dict()

    with open(path, 'r') as file_handler:
        dictionary = file_handler.read()

    results["unfiltered"] = lossy_compression_tools.frequency(dictionary)

    dictionary = lossy_compression_tools.remove_numbers(dictionary)
    results["no_number"] = lossy_compression_tools.frequency(dictionary)

    dictionary = lossy_compression_tools.case_folding(dictionary)
    results["case_folding"] = lossy_compression_tools.frequency(dictionary)

    dictionary = lossy_compression_tools.remove_stopwords(dictionary, 30)
    results["30_stopwords"] = lossy_compression_tools.frequency(dictionary)

    dictionary = lossy_compression_tools.remove_stopwords(dictionary, 150)
    results["150_stopwords"] = lossy_compression_tools.frequency(dictionary)

    dictionary = lossy_compression_tools.stemming(dictionary)
    results["stemming"] = lossy_compression_tools.frequency(dictionary)

    return results


def getCompressedDictionary(path):
    dictionary = dict()
    stats = dict()

    with open(path, 'r') as file_handler:
        dictionary = file_handler.read()

    dictionary = lossy_compression_tools.remove_numbers(dictionary)
    dictionary = lossy_compression_tools.case_folding(dictionary)
    dictionary = lossy_compression_tools.remove_stopwords(dictionary, 30)
    dictionary = lossy_compression_tools.remove_stopwords(dictionary, 150)
    dictionary = lossy_compression_tools.stemming(dictionary)

    return dictionary


def displayTable(path):
    term_data = computeTermLossy(path)
    np_data = computeNonPopLossy(path)

    print("\n\t\t\tTerms\t\tNP Postings")
    print("-" * 60)
    print("\t\tfreq\tΔ%\tT%\tfreq\tΔ%\tT%")
    print("-" * 60)

    print(f'unfiltered\t{term_data["unfiltered"]}\t\t\t{np_data["unfiltered"]}')

    delta_value_terms = lossy_compression_tools.delta(term_data["unfiltered"], term_data["no_number"])
    term_value_terms = lossy_compression_tools.delta(term_data["unfiltered"], term_data["no_number"])
    delta_value_np = lossy_compression_tools.delta(np_data["unfiltered"], np_data["no_number"])
    term_value_np = lossy_compression_tools.delta(np_data["unfiltered"], np_data["no_number"])
    print(
        f'no numbers\t{term_data["no_number"]}\t{delta_value_terms * -1 if delta_value_terms > 0 else delta_value_terms}\t{term_value_terms * -1 if term_value_terms > 0 else term_value_terms}\t{np_data["no_number"]}\t{delta_value_np * -1}\t{term_value_np * -1}')

    delta_value_terms = lossy_compression_tools.delta(term_data["no_number"], term_data["case_folding"])
    term_value_terms = lossy_compression_tools.delta(term_data["unfiltered"], term_data["case_folding"])
    delta_value_np = lossy_compression_tools.delta(np_data["no_number"], np_data["case_folding"])
    term_value_np = lossy_compression_tools.delta(np_data["unfiltered"], np_data["case_folding"])
    print(
        f'case folding\t{term_data["case_folding"]}\t{delta_value_terms * -1 if delta_value_terms > 0 else delta_value_terms}\t{term_value_terms * -1 if term_value_terms > 0 else term_value_terms}\t{np_data["case_folding"]}\t{delta_value_np * -1}\t{term_value_np * -1}')

    delta_value_terms = lossy_compression_tools.delta(term_data["case_folding"], term_data["30_stopwords"])
    term_value_terms = lossy_compression_tools.delta(term_data["unfiltered"], term_data["30_stopwords"])
    delta_value_np = lossy_compression_tools.delta(np_data["case_folding"], np_data["30_stopwords"])
    term_value_np = lossy_compression_tools.delta(np_data["unfiltered"], np_data["30_stopwords"])
    print(
        f'30 stopwords\t{term_data["30_stopwords"]}\t{delta_value_terms * -1 if delta_value_terms > 0 else delta_value_terms}\t{term_value_terms * -1 if term_value_terms > 0 else term_value_terms}\t{np_data["30_stopwords"]}\t{delta_value_np * -1}\t{term_value_np * -1}')

    delta_value_terms = lossy_compression_tools.delta(term_data["30_stopwords"], term_data["150_stopwords"])
    term_value_terms = lossy_compression_tools.delta(term_data["unfiltered"], term_data["150_stopwords"])
    delta_value_np = lossy_compression_tools.delta(np_data["30_stopwords"], np_data["150_stopwords"])
    term_value_np = lossy_compression_tools.delta(np_data["unfiltered"], np_data["150_stopwords"])
    print(
        f'150 stopwords\t{term_data["150_stopwords"]}\t{delta_value_terms * -1 if delta_value_terms > 0 else delta_value_terms}\t{term_value_terms * -1 if term_value_terms > 0 else term_value_terms}\t{np_data["150_stopwords"]}\t{delta_value_np * -1}\t{term_value_np * -1}')

    delta_value_terms = lossy_compression_tools.delta(term_data["150_stopwords"], term_data["stemming"])
    term_value_terms = lossy_compression_tools.delta(term_data["unfiltered"], term_data["stemming"])
    delta_value_np = lossy_compression_tools.delta(np_data["150_stopwords"], np_data["stemming"])
    term_value_np = lossy_compression_tools.delta(np_data["unfiltered"], np_data["stemming"])
    print(
        f'stemming\t{term_data["stemming"]}\t{delta_value_terms * -1 if delta_value_terms > 0 else delta_value_terms}\t{term_value_terms * -1 if term_value_terms > 0 else term_value_terms}\t{np_data["stemming"]}\t{delta_value_np * -1}\t{term_value_np * -1}')
    print('\n')
