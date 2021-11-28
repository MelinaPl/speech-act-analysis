# -*- coding: utf-8 -*-
"""
@author: Melina Plakidis
"""
import os
import json
import xml.etree.ElementTree as ET
import fire
import json

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r


def transform(inp_dir, out_dir):
   # transforms downloaded INCEpTION dataset into a more readable format 
    all_files = list_files(inp_dir)
    for file in all_files:
        file_name = file.split("/")
        file_name = file_name[2].split("\\")
        file_name = file_name[0].replace(".txt", "")    
        other_file = out_dir + file_name + ".xml"
        with open(file, 'r', encoding='utf8') as inp, open (other_file, "w", encoding="utf8") as out:
            lines = inp.readlines()
            for line in lines:
                out.write(line)

# Evaluation: The two following methods are pre-processing steps for the
# statistical analysis

def read_tweet(tweet_file):
    tree = ET.parse(tweet_file)
    root = tree.getroot()
    scount = 0
    coarse, fine, stype = [], [], []
    tweet = {}
    sentences = {}
    for children in root:
        #print(children.attrib['language'])
        for child in children:
            sentence = {}
            print(child.tag)
            for c in child:
                if c.tag == "custom.Span":
                    scount += 1
                    coarse.append([scount, c.attrib["CoarseSA"]])
                    fine.append(c.attrib["FineSA"])
                    stype.append(c.attrib["stype"])
                    sentence = {"stype":c.attrib["stype"], "coarse" : c.attrib["CoarseSA"], "fine" : c.attrib["FineSA"]}
                    sentences[scount] = sentence                
    if len(sentences) == 0:
        sentences = {}
        scount = 0
        coarse, fine, stype = [], [], []
        for children in root:
            #print(children.attrib['language'])
            sentence = {}
            for child in children:
                sentence = {}
                if child.tag == "custom.Span":
                    scount += 1
                    coarse.append([scount, child.attrib["CoarseSA"]])
                    fine.append(child.attrib["FineSA"])
                    stype.append(child.attrib["stype"])
                    sentence = {"stype":child.attrib["stype"], "coarse" : child.attrib["CoarseSA"], "fine" : child.attrib["FineSA"]}
                    sentences[scount] = sentence           
    tweet["tweet"] = {"scount": scount, "sentences" : sentences}
    return tweet
                
    
def write_json (data_dir, outfile): 
    # transforms all annotated XML files into one JSON file
    files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
    tweets = {}
    for f in files:
        f = data_dir +f
        tweet = read_tweet(f)
        tweets[f.replace(data_dir, "")] = tweet
    with open(outfile, 'w') as out:
        json.dump(tweets, out, indent=4)
    


if __name__=='__main__':           
    fire.Fire() 
#    transform("Speech+Act+Analysis+PII_curated_documents_2021-10-03_1645/curation/")
#    write_json("dataset_annotated_complete/", "data.json")
