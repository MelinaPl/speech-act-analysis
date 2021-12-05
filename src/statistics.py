# -*- coding: utf-8 -*-

"""
@author: Melina Plakidis
"""

import os
import json
import re 
import xml.etree.ElementTree as ET
import random
import fire
import pandas as pd
import numpy as np
import csv


with open("data.json", 'r') as inp:
    dataset = json.load(inp)
    print(len(dataset)) # zurzeit 589
    for tweet in dataset:
        print(tweet) # filename
        doc = dataset[tweet] # {'tweet': {'scount': 2, 'sentences': {'1': {'stype': 'ment', 'coarse': 'DIRECTIVE', 'fine': 'ADDRESS'}, '2': {'stype': 'decl', 'coarse': 'ASSERTIVE', 'fine': 'ASSERT'}}}}
        print(doc["tweet"]["scount"]) # prints int of sentence count


# count sentences in offensive language categories and write in table
        
with open("data.json", 'r') as inp, open("statistics_hs_senttype.tsv", "a", encoding = "utf8") as out:
    data = json.load(inp)
    header = ['','Other', 'Implicit', 'Explicit', 'Abuse', 'Profanity', 'Insult', "Total"]
    #header = ["alt-f", "decl", "excl", "f", "frag", "hashtag", "imp", "intj", "kon", "ment", "mult", "non-txt", "other", "w-f"]
    writer = csv.writer(out,dialect='excel-tab')
    writer.writerow(header)
    other_count, impl_count, expl_count, ab_count, pr_count, in_count, total = 0,0,0,0,0,0,0
    for ele in data:
        name = ele
        tweet = data[ele]
        for value in tweet.values():
            scount = value['scount']
            total += scount
            if "other" in name:
                    hs_type = "other"
                    other_count += scount
            elif "implicit" in name:
                hs_type = "implicit"
                impl_count += scount
            elif "explicit" in name:
                hs_type = "explicit"
                expl_count += scount
            elif "abuse" in name: 
                    hs_type = "abuse"
                    ab_count += scount
            elif "profanity" in name:
                hs_type = "profanity"
                pr_count += scount
            elif "insult" in name:
                hs_type = "insult"
                in_count += scount
    no_sents = ['Number of sentences', other_count, impl_count, expl_count, ab_count, pr_count, in_count, total]
    writer.writerow(no_sents)


# example how sentences were counted for each annotation class for every 
# offensive language category
with open("data.json", 'r') as inp, open("statistics_hs_stype_fine.tsv", "a", encoding = "utf8") as out:
    data = json.load(inp)
    writer = csv.writer(out,dialect='excel-tab')
    header = ["alt-f", "decl", "excl", "f", "frag", "hashtag", "imp", "intj", "kon", "ment", "mult", "non-txt", "other", "w-f"]
    #header = ['','Other', 'Implicit', 'Explicit', 'Abuse', 'Profanity', 'Insult', "Total"]
    writer.writerow(header)
    other_count, impl_count, expl_count, ab_count, pr_count, in_count, total = 0,0,0,0,0,0,0
    for ele in data:
        name = ele
        tweet = data[ele]
        for value in tweet.values():
            sentences = value['sentences']
            for sentence in sentences:
                stype = sentences[sentence]['stype']
                coarse = sentences[sentence]['coarse']
                fine = sentences[sentence]['fine']
                if stype == "alt-f":
                    total += 1
                    if "other" in name:
                            hs_type = "other"
                            other_count += 1
                    elif "implicit" in name:
                        hs_type = "implicit"
                        impl_count += 1
                    elif "explicit" in name:
                        hs_type = "explicit"
                        expl_count += 1
                    elif "abuse" in name: 
                            hs_type = "abuse"
                            ab_count += 1
                    elif "profanity" in name:
                        hs_type = "profanity"
                        pr_count += 1
                    elif "insult" in name:
                        hs_type = "insult"
                        in_count += 1
    no_sents = ['alt-f', other_count, impl_count, expl_count, ab_count, pr_count, in_count, total]
    writer.writecolumn(no_sents)

##### Used for creating the table: coarse-grained labels x sentence types
with open("data.json", 'r') as inp, open("statistics_stype_coarse.tsv", "w", encoding = "utf8") as out:
    data = json.load(inp)
    writer = csv.writer(out,dialect='excel-tab')
    senttypes = ["alt-f", "decl", "excl", "f", "frag", "hashtag", "imp", "intj", "kon", "ment", "mult", "non-txt", "other", "w-f"]
    header = ['','ASSERTIVE', 'COMMISSIVE', 'EXPRESSIVE', 'DIRECTIVE', 'UNSURE', 'OTHER', 'TOTAL']
    writer.writerow(header)
    for s in senttypes:
        as_count, com_count, exp_count, dir_count, un_count, oth_count, total = 0,0,0,0,0,0,0
        total_as, total_com, total_exp, total_dir, total_un, total_oth, total_all = 0,0,0,0,0,0,0
        for ele in data:
            name = ele
            tweet = data[ele]
            for value in tweet.values():
                sentences = value['sentences']
                for sentence in sentences:
                    stype = sentences[sentence]['stype']
                    coarse = sentences[sentence]['coarse']
                    fine = sentences[sentence]['fine']
                    total_all += 1
                    if coarse == "ASSERTIVE":
                        total_as += 1
                    elif coarse == "COMMISSIVE":
                        total_com += 1
                    elif coarse == "EXPRESSIVE":
                        total_exp += 1
                    elif coarse == "DIRECTIVE": 
                        total_dir += 1
                    elif coarse == "UNSURE": 
                        total_un += 1
                    elif coarse == "OTHER": 
                        total_oth += 1
                    if stype == s:
                        total += 1
                        if coarse == "ASSERTIVE":
                                as_count += 1
                        elif coarse == "COMMISSIVE":
                            com_count += 1
                        elif coarse == "EXPRESSIVE":
                            exp_count += 1
                        elif coarse == "DIRECTIVE": 
                                dir_count += 1
                        elif coarse == "UNSURE": 
                                un_count += 1
                        elif coarse == "OTHER": 
                                oth_count += 1
        no_sents = [s, as_count, com_count, exp_count, dir_count, un_count, oth_count, total]
        writer.writerow(no_sents)
    total = ["Total", total_as, total_com, total_exp, total_dir, total_un, total_oth, total_all]
    writer.writerow(total)

#### Used for creating the table: fine-grained labels x sentence types
with open("data.json", 'r') as inp, open("statistics_stype_fine2.tsv", "w", encoding = "utf8") as out:
    data = json.load(inp)
    writer = csv.writer(out,dialect='excel-tab')
    header = ["","alt-f", "decl", "excl", "f", "frag", "hashtag", "imp", "intj", "kon", "ment", "mult", "non-txt", "other", "w-f"]
    fines = ['ACCEPT', 'ADDRESS', 'AGREE', 'APOLOGIZE', 'ASSERT', 'COMPLAIN', 'DISAGREE', 'ENGAGE', 'GREET', 'GUESS', 'OTHER', 'PREDICT', 'REFUSE', 'REJOICE', 'REQUEST', 'REQUIRE', 'SUGGEST', 'SUSTAIN', 'THANK', 'THREAT', 'UNSURE', 'WISH', 'expressEMOJI']
    writer.writerow(header)
    for f in fines:
        altf_count, decl_count, excl_count, f_count, frag_count, hash_count, imp_count, intj_count, kon_count, ment_count, mult_count, non_count, oth_count, wf_count, total = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        total_altf, total_decl, total_excl, total_f, total_frag, total_hash, total_imp, total_intj, total_kon, total_ment, total_mult, total_non, total_oth, total_wf, total_all = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        for ele in data:
            name = ele
            tweet = data[ele]
            for value in tweet.values():
                sentences = value['sentences']
                for sentence in sentences:
                    stype = sentences[sentence]['stype']
                    coarse = sentences[sentence]['coarse']
                    fine = sentences[sentence]['fine']
                    total_all += 1
                    if stype == "alt-f":
                        total_altf += 1
                    elif stype == "decl":
                        total_decl += 1
                    elif stype == "excl":
                        total_excl += 1
                    elif stype == "f": 
                        total_f += 1
                    elif stype == "frag": 
                        total_frag += 1
                    elif stype == "hashtag": 
                        total_hash += 1
                    elif stype == "imp":
                        total_imp += 1
                    elif stype == "intj":
                        total_intj += 1
                    elif stype == "kon": 
                        total_kon += 1
                    elif stype == "ment": 
                        total_ment += 1
                    elif stype == "mult": 
                        total_mult += 1
                    elif stype == "non-txt":
                        total_non += 1
                    elif stype == "other":
                        total_oth += 1
                    elif stype == "w-f": 
                        total_wf += 1
                    if fine == f:
                        total += 1
                        if stype == "alt-f":
                            altf_count += 1
                        elif stype == "decl":
                            decl_count += 1
                        elif stype == "excl":
                            excl_count += 1
                        elif stype == "f": 
                            f_count += 1
                        elif stype == "frag": 
                            frag_count += 1
                        elif stype == "hashtag": 
                            hash_count += 1
                        elif stype == "imp":
                            imp_count += 1
                        elif stype == "intj":
                            intj_count += 1
                        elif stype == "kon": 
                            kon_count += 1
                        elif stype == "ment": 
                            ment_count += 1
                        elif stype == "mult": 
                            mult_count += 1
                        elif stype == "non-txt":
                            non_count += 1
                        elif stype == "other":
                            oth_count += 1
                        elif stype == "w-f": 
                            wf_count += 1
        no_sents = [f, altf_count, decl_count, excl_count, f_count, frag_count, hash_count, imp_count, intj_count, kon_count, ment_count, mult_count, non_count, oth_count, wf_count, total]
        writer.writerow(no_sents)
    total = ["Total", total_altf, total_decl, total_excl, total_f, total_frag, total_hash, total_imp, total_intj, total_kon, total_ment, total_mult, total_non, total_oth, total_wf, total_all]
    writer.writerow(total)
                
            