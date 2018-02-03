#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 13:51:10 2017

@author: anjana
"""

from nltk import bigrams, trigrams
from nltk import word_tokenize
from collections import Counter

    
text = '/home/anjana/Anjana/NLC/text_input.txt'


with open(text) as f:
    p = f.read()   
    tokens = word_tokenize(p)
    size = len(tokens)
    bi = list(bigrams(tokens, pad_left=True, pad_right=True)) # Get the padded bigrams
    size_bi = len(bi)
    
    tri = list(trigrams(tokens, pad_left=True, pad_right=True))
    size_tri = len(tri)
    
    string = str(input())
    tok = word_tokenize(string)
    
    bi_str = list(bigrams(tok, pad_left=True, pad_right=True))
    size_bi_str = len(bi_str)
    bi_test = bi_str
    
    tri_str = list(trigrams(tok, pad_left=True, pad_right=True))
    tri_test = tri_str
    size_tri_str = len(tri_str)
    
    prob_bi = (tokens.count(tok[0])/size) * (bi.count(bi_str[1])/size_bi)
    
    search = bi_str[size_bi_str-1][0]
    maxi = 0
    for sublist in bi:
        if sublist[0] == search:
            bi_test[size_bi_str-1] = sublist
            for i in range(2, len(bi_test)-1):
                prob_bi = prob_bi * (bi.count(bi_test[i])/tok.count(bi_test[i][0]))
                
            if ( maxi < prob_bi):
                maxi = prob_bi
                string_final = bi_test
    #print (string_final)
    print ("bigram: " + string + " " + string_final[len(bi_test)-1][1])
    
    search = tri_str[size_tri_str-2][0:1]
    maxi = 0
    prob_tri = prob_bi
    for sublist in tri:
        if sublist[0:1] == search:
            tri_test[size_tri_str-2] = sublist
            tri_test = tri_test[0:size_tri_str-1]
            for i in range(2, len(tri_test)-1):
                prob_tri = prob_tri * (tri.count(tri_test[i])/size_tri)
            
            if ( maxi < prob_bi):
                maxi = prob_tri
                string_final = tri_test

    print ("trigram: " + string + " " + string_final[len(tri_test)-1][2])



