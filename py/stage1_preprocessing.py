# EECS 4412 - Data Mining
# Stage 1 Preprocessing: stage1_preprocessing.py
# Author: Gian Carlo Alix

# import necessary libraries
import pandas as pd
import numpy as np
import re

def merge_tokens(lst):
    # use this to merge a list of tokens into a full line sentence
    line = ""
    for token in lst:
        line = line + token + " "
    return line

def remove_stopwords(tokens,stop_list):
    # returns a list without stopwords
    new_tokens = []
    for i in range(len(tokens)):
        if tokens[i].lower() not in stop_list:
            new_tokens.append(tokens[i].lower())
    return new_tokens

def preprocess(sentence,stop_list):
    # split using regex
    regex = "[/\$()\[\]!?%&*:.=\^,\+\s\t\n#]"
    tokens = re.split(regex, sentence)
    
    # remove stopwords
    new_tokens = remove_stopwords(tokens,stop_list)
    ln = merge_tokens(new_tokens)
    return ln

def stage1(df,sw,dataset,drop_cols):
    # drop certain columns
    df = df.drop(drop_cols, axis=1)

    # preprocess here
    for i in range(len(df)):
	    df['text'][i] = preprocess(df['text'][i], sw)
    
    # output to a file
    filename = dataset + "_set_stage1_preprocessed.csv"
    df.to_csv(filename,index=False,header=False)
    print("Stage 1 Preprocessing Complete for " + dataset + "_set completed!")

def main():
    # import the datasets
    df_train = pd.read_csv("data/train3.csv")
    df_test = pd.read_csv("data/test3.csv")
    sw = pd.read_csv("stopwords.csv")

    # to eliminate numbers and empty strings,
    # we treat these as stopwors to remove. 
    # create a file called more_stopwords.csv 
    list_of_more_stopwords = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '']
    sw_additional = pd.DataFrame({'stopwords':list_of_more_stopwords})
    sw_additional.to_csv("more_stopwords.csv",index=False)

    # merge the stopwords into a single list
    sw = sw.append(sw_additional)

    # stage1 preprocessing
    stage1(df_train, list(sw['stopwords']), "train",['class','ID'])
    stage1(df_test, list(sw['stopwords']), "test",['ID'])

main()