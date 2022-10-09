import json

from Project_2.subproject3 import lossy_dict
import pandas as pd

"""
The following lossy_compression file will be used soley to compute len() of the lossy dictionary compression techniques
while creating the table for Reuters-21578
"""

"""
Compute lossy terms of each category
@:param path of the posting_list.json 
@:return the stats of each caterogy in numerical value
"""


def compute_term_lossy(path):
    dictionary = dict()
    stats = dict()

    with open(path, 'r') as json_file:
        dictionary = json.load(json_file)

    stats["unfiltered"] = len(dictionary)

    dictionary = lossy_dict.remove_numbers(dictionary)
    stats["no_number"] = len(dictionary)

    dictionary = lossy_dict.case_folding(dictionary)
    stats["case_folding"] = len(dictionary)

    dictionary = lossy_dict.remove_stopwords(dictionary, 30)
    stats["30_stopwords"] = len(dictionary)

    dictionary = lossy_dict.remove_stopwords(dictionary, 150)
    stats["150_stopwords"] = len(dictionary)

    dictionary = lossy_dict.stemming(dictionary)
    stats["stemming"] = len(dictionary)

    return stats


"""
Compute the frequency of each category in 
@:param path of the posting_list.json 
@:return the stats of each caterogy in numerical value
"""


def compute_non_propositional_lossy(path):
    dictionary = dict()
    stats = dict()

    with open(path, 'r') as json_file:
        dictionary = json.load(json_file)

    stats["unfiltered"] = lossy_dict.frequency(dictionary)

    dictionary = lossy_dict.remove_numbers(dictionary)
    stats["no_number"] = lossy_dict.frequency(dictionary)

    dictionary = lossy_dict.case_folding(dictionary)
    stats["case_folding"] = lossy_dict.frequency(dictionary)

    dictionary = lossy_dict.remove_stopwords(dictionary, 30)
    stats["30_stopwords"] = lossy_dict.frequency(dictionary)

    dictionary = lossy_dict.remove_stopwords(dictionary, 150)
    stats["150_stopwords"] = lossy_dict.frequency(dictionary)

    dictionary = lossy_dict.stemming(dictionary)
    stats["stemming"] = lossy_dict.frequency(dictionary)

    return stats


"""
Compress the terms in each category  
@:param path of the posting_list.json 
@:return the dic() value 
"""


def get_compressed_dictionary(path):
    dictionary = dict()
    stats = dict()

    with open(path, 'r') as json_file:
        dictionary = json.load(json_file)

    dictionary = lossy_dict.remove_numbers(dictionary)
    dictionary = lossy_dict.case_folding(dictionary)
    dictionary = lossy_dict.remove_stopwords(dictionary, 30)
    dictionary = lossy_dict.remove_stopwords(dictionary, 150)
    dictionary = lossy_dict.stemming(dictionary)

    return dictionary


"""
Create informational table of words types, non-positional , positional postings
@:param path of the posting_list.json 
@:return the stats of each caterogy in numerical value
"""


def display_table(path):
    term_data = compute_term_lossy(path)
    np_data = compute_non_propositional_lossy(path)

    print("-" * 80)
    column_names = pd.DataFrame([["Terms", "Frequency"],
                                 ["", "Δ%"],
                                 ["", "T%"],
                                 ["Non-Positional Postings", "Frequency"],
                                 ["", "Δ%"],
                                 ["", "T%"]],
                                columns=["", ""])

    no_num_delta_value_terms = lossy_dict.delta(term_data["unfiltered"], term_data["no_number"])
    no_num_term_value_terms = lossy_dict.delta(term_data["unfiltered"], term_data["no_number"])
    no_num_delta_value_np = lossy_dict.delta(np_data["unfiltered"], np_data["no_number"])
    no_num_term_value_np = lossy_dict.delta(np_data["unfiltered"], np_data["no_number"])

    cf_delta_value_terms = lossy_dict.delta(term_data["no_number"], term_data["case_folding"])
    cf_term_value_terms = lossy_dict.delta(term_data["unfiltered"], term_data["case_folding"])
    cf_delta_value_np = lossy_dict.delta(np_data["no_number"], np_data["case_folding"])
    cf_term_value_np = lossy_dict.delta(np_data["unfiltered"], np_data["case_folding"])

    sw_delta_value_terms = lossy_dict.delta(term_data["case_folding"], term_data["30_stopwords"])
    sw_term_value_terms = lossy_dict.delta(term_data["unfiltered"], term_data["30_stopwords"])
    sw_delta_value_np = lossy_dict.delta(np_data["case_folding"], np_data["30_stopwords"])
    sw_term_value_np = lossy_dict.delta(np_data["unfiltered"], np_data["30_stopwords"])

    sw150_delta_value_terms = lossy_dict.delta(term_data["30_stopwords"], term_data["150_stopwords"])
    sw150_term_value_terms = lossy_dict.delta(term_data["unfiltered"], term_data["150_stopwords"])
    sw150_delta_value_np = lossy_dict.delta(np_data["30_stopwords"], np_data["150_stopwords"])
    sw150_term_value_np = lossy_dict.delta(np_data["unfiltered"], np_data["150_stopwords"])

    stem_delta_value_terms = lossy_dict.delta(term_data["150_stopwords"], term_data["stemming"])
    stem_term_value_terms = lossy_dict.delta(term_data["unfiltered"], term_data["stemming"])
    stem_delta_value_np = lossy_dict.delta(np_data["150_stopwords"], np_data["stemming"])
    stem_term_value_np = lossy_dict.delta(np_data["unfiltered"], np_data["stemming"])

    rows = [[term_data["unfiltered"], "", "", np_data["unfiltered"], "", ""],
            [term_data["no_number"],
             no_num_delta_value_terms * -1 if no_num_delta_value_terms > 0 else no_num_delta_value_terms,
             no_num_term_value_terms * -1 if no_num_term_value_terms > 0 else no_num_term_value_terms,
             np_data["no_number"],
             no_num_delta_value_np * -1, no_num_term_value_np * -1],
            [term_data["case_folding"], cf_delta_value_terms * -1 if cf_delta_value_terms > 0 else cf_delta_value_terms,
             cf_term_value_terms * -1 if cf_term_value_terms > 0 else cf_term_value_terms, np_data["case_folding"],
             cf_delta_value_np * -1, cf_term_value_np * -1],
            [term_data["30_stopwords"], sw_delta_value_terms * -1 if sw_delta_value_terms > 0 else sw_delta_value_terms,
             sw_term_value_terms * -1 if sw_term_value_terms > 0 else sw_term_value_terms, np_data["30_stopwords"],
             sw_delta_value_np * -1, sw_term_value_np * -1],
            [term_data["150_stopwords"],
             sw150_delta_value_terms * -1 if sw150_delta_value_terms > 0 else sw150_delta_value_terms,
             sw150_term_value_terms * -1 if sw150_term_value_terms > 0 else sw150_term_value_terms,
             np_data["150_stopwords"],
             sw150_delta_value_np * -1, sw150_term_value_np * -1],
            [term_data["stemming"],
             stem_delta_value_terms * -1 if stem_delta_value_terms > 0 else stem_delta_value_terms,
             stem_term_value_terms * -1 if stem_term_value_terms > 0 else stem_term_value_terms, np_data["stemming"],
             stem_delta_value_np * -1, stem_term_value_np * -1]]

    print("-" * 80)
    columns = pd.MultiIndex.from_frame(column_names)

    index = ["unfiltered:", "no_numbers:", "case_folding:", "30_stopwords:", "150_stopwords:", "stemming:"]

    display_table_pd = pd.DataFrame(rows, columns=columns, index=index)
    print(display_table_pd)
    print("-" * 80)
