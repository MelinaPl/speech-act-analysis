# -*- coding: utf-8 -*-
"""
@author: Melina
"""

from os import listdir
from os.path import isfile, join
import json
import re 
import xml.etree.ElementTree as ET
import random


# Write indexes so every tweet can be identified

with open('original_files/germeval2019GoldLabelsSubtask3.txt', 'r', encoding='utf8') as inp:
    lines = inp.readlines()
    indexno = 0
    with open('files_with_indexes/ind_germeval2019GoldLabelsSubtask3.txt','w', encoding='utf16') as out:            
        for line in lines:
           out.write("<<@"+ str(indexno)+">>") 
           out.write(line)
           indexno += 1

# Generate shuffled index files

with open('files_with_indexes/ind_germeval2019GoldLabelsSubtask3.txt', 'r', encoding='utf16') as inp, open('files_with_indexes/ind_shuffle_germeval2019GoldLabelsSubtask3.txt', 'w', encoding='utf16') as out:
    lines = inp.readlines()
    random.shuffle(lines)
    for line in lines:
        out.write(line)

# write .txt files from subtask 1 and 2 and allocate them to their respective directories
           
with open('D:/HS_py/files_with_indexes/ind_shuffle_germeval2019GoldLabelsSubtask1_2.txt', 'r', encoding='utf16') as inp:
    lines = inp.readlines()
    nr = 0
    for line in lines:        
       match = re.findall("<<@[0-9]+>>", line)
       index = match[0].strip("<<@").strip(">>")
       print(index)
       line = re.sub("<<@"+str(index)+">>", "", line)
       no_tag = re.sub("\t[A-Z]+\t[A-Z]+\n", "", line)
       if "OTHER" in line:
           with open('data/no_hs/s1-2_Tweet_'+ str(nr)+ "_" + str(index) + '_other'+'.txt','w', encoding='utf16') as no_hs:
               no_hs.write(no_tag)
       elif "ABUSE" in line:
           with open('data/hs_without_impl_expl/abuse/s1-2_Tweet_'+ str(nr)+ "_" +  str(index) + '_abuse' +'.txt','w', encoding='utf16') as abuse:
               abuse.write(no_tag)
       if "PROFANITY" in line:
           with open('data/hs_without_impl_expl/profanity/s1-2_Tweet_'+ str(nr)+ "_" + str(index) + '_profanity' +'.txt','w', encoding='utf16') as profanity:
               profanity.write(no_tag)
       if "INSULT" in line:
           with open('data/hs_without_impl_expl/insult/s1-2_Tweet_'+ str(nr)+ "_" +  str(index) + '_insult' +'.txt','w', encoding='utf16') as insult:
               insult.write(no_tag)
       nr += 1

# write .txt files from subtask 3 and allocate them to their respective directories

with open('D:/HS_py/files_with_indexes/ind_shuffle_germeval2019GoldLabelsSubtask3.txt', 'r', encoding='utf16') as inp:
    lines = inp.readlines()
    nr = 0
    for line in lines:
       match = re.findall("<<@[0-9]+>>", line)
       index = match[0].strip("<<@").strip(">>")
       print(index)
       line = re.sub("<<@"+str(index)+">>", "", line)
       line = re.sub("<<@"+str(index)+">>", "", line)
       no_tag = re.sub("\t[A-Z]+\t[A-Z]+\t[A-Z]+\n", "", line)
       print(no_tag)
       if "EXPLICIT" in line:
           with open('data/impl_expl/expl/s3_Tweet_'+ str(nr)+ "_" + str(index) + '_explicit' +'.txt','w', encoding='utf-8') as expl:
               expl.write(no_tag)
       elif "IMPLICIT" in line:
           with open('data/impl_expl/impl/s3_Tweet_'+ str(nr)+ "_" + str(index) + '_implicit' +'.txt','w', encoding='utf-8') as impl:
               impl.write(no_tag)
       nr += 1


######## Clean tweets (fix emojis) ################


def convert_emojis(line):   
# !!!! ONLY USE FOR DATASET SUBTASK 1 + 2 !!!!     
    emojis = re.findall("<U\+[a-zA-Z0-9_]+>", line)
    emoji_count = 0
    newline = line
    for emoji in emojis:
        emoji_count += 1
        if emoji_count == 1:
            conv_emoji = emoji.replace("<", "\\").replace(">", "").replace("+", "")
            encoded = conv_emoji.encode("utf-8")
            print(conv_emoji)
            print(encoded)
            try:
                decoded = encoded.decode("unicode-escape")
            except:
                decoded = encoded.decode("utf-8")
            newline = line.replace(emoji, decoded)
        else: 
            oldline = newline
            conv_emoji = emoji.replace("<", "\\").replace(">", "").replace("+", "")
            encoded = conv_emoji.encode("utf-8")
            print(conv_emoji)
            print(encoded)
            try:
                decoded = encoded.decode("unicode-escape")
            except:
                decoded = encoded.decode("utf-8")
            newline = oldline.replace(emoji, decoded)
    return newline

def clean_tweet(line):
    newline = convert_emojis(line)
    newline = re.sub("\\\"\"", "\"", newline)
    newline = re.sub(r'\\"', "\"", newline)
#  include if linebreaks should be removed from tweet ########
#    if "|LBR|" in newline:
#        newline = newline.replace("|LBR|", "")
    return newline
    
    
# clean all tweets from subtask 1 + 2

def clean_s12():    
    with open('D:/HS_py/files_with_indexes/con_ind_shuffle_germeval2019GoldLabelsSubtask1_2.txt', 'r', encoding='utf-8') as inp:
        lines = inp.readlines()
        nr = 0
        for line in lines:
            nr += 1
            match = re.findall("<<@[0-9]+>>", line)
            index = match[0].strip("<<@").strip(">>")
            line = re.sub("<<@"+str(index)+">>", "", line)
            no_tag = re.sub("\t[A-Z]+\t[A-Z]+\n", "", line)
            if "OTHER" in line:
                with open('data/no_hs/s1-2_Tweet_'+ str(nr)+ "_" + str(index) + '_other'+'.txt','w', encoding='utf-8') as no_hs:
                    no_tag = clean_tweet(no_tag)
                    print(no_tag)
                    no_hs.write(no_tag)
            elif "ABUSE" in line:
                with open('data/hs_without_impl_expl/abuse/s1-2_Tweet_'+ str(nr)+ "_" +  str(index) + '_abuse' +'.txt','w', encoding='utf-8') as abuse:
                    no_tag = clean_tweet(no_tag)
                    print(no_tag)
                    abuse.write(no_tag)
            elif "PROFANITY" in line:
                with open('data/hs_without_impl_expl/profanity/s1-2_Tweet_'+ str(nr)+ "_" + str(index) + '_profanity' +'.txt','w', encoding='utf-8') as profanity:
                    no_tag = clean_tweet(no_tag)
                    print(no_tag)
                    profanity.write(no_tag)
            elif "INSULT" in line:
                with open('data/hs_without_impl_expl/insult/s1-2_Tweet_'+ str(nr)+ "_" +  str(index) + '_insult' +'.txt','w', encoding='utf-8') as insult:
                    no_tag = clean_tweet(no_tag)
                    print(no_tag)
                    insult.write(no_tag)
                
     
