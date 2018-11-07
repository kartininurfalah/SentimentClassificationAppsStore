#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 22:25:01 2018

@author: helmisatria
"""

import nltk
# from nltk import word_tokenize
import csv
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
stemming = PorterStemmer()
import re
import numpy as np
from collections import Counter
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

data = [] 

# with open('SentimentDatasetonAppReviewfromAppStore.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in data:
#         data.append(row)
#         print(', '.join(row))

        
with open('SentimentDatasetonAppReviewfromAppStore.csv', 'r') as f:
    reader = csv.reader(f)
    firstline = reader
    
    # texts = [[word.lower() for word in text.split()] for text in reader]
    for idx,row in enumerate(firstline):
        # cleanWords = (re.sub(r'[.,\/#!$%\^&\*;:{}=\-_+`~()\'\"{0-9}]', ' ',row.lower()))
        
        data.append(row)
        # print(row)

        # data = [x.strip() for x in row]
       
# texts = [[word.lower() for word in text.split()] for text in data]   

     
def Cleaning(AllDocuments):
    cleandoc = []
    for i, document in enumerate(AllDocuments):
        # print(document)
        cleanContent = []
        for j, content in enumerate(document):
            print(content)
            if j == 0 :
                cleanContent.append(content)
                continue
            stopWords = stopword.remove(content)
            cleanWords = (re.sub(r'[.,\/#!$%\^&\*;:{}=\-_+`~()\'\"{0-9}]', ' ',stopwords.lower()))
            words = word_tokenize(cleanWords)
            wordsFilteredStemmed = []
            
            for w in words:
                if w not in stopWords:
                    wordsFilteredStemmed.append(stemming.stem(w))
            
            cleanContent.append(wordsFilteredStemmed)
            
        cleandoc.append(cleanContent)
    
    return cleandoc

datacllean = Cleaning(data)