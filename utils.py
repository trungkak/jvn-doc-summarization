# -*- coding: utf-8 -*-
# Utils functions for pre-processing text data
#

from nltk.tokenize import wordpunct_tokenize, sent_tokenize
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))


def word_split(sent):
    """ Tokenize a sentence into tokens """
    tokens = wordpunct_tokenize(sent)
    tokens = [tok.lower() for tok in tokens if tok.isalpha() and tok not in stopwords]
    return tokens


def sent_split(doc):
    """ Split a document into sentences (list of strings) """
    sentences = sent_tokenize(doc)
    return sentences
