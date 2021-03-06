#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
#from nltk.corpus import stopwords
#from nltk.stem import RSLPStemmer
import re
from sklearn.externals import joblib


def review_to_words(review):

    if isinstance(review, float):
        review = str(review).encode("utf-8")
    letters_only = re.sub("\W+", " ", review, flags=re.UNICODE)

    words = letters_only.lower().split()
    #nltk.data.path.append('./nltk_data/')
    #stops = set(nltk.corpus.stopwords.words("portuguese"))
    meaningful_words = words #[w for w in words if not w in stops]
    #stemmer = RSLPStemmer()
    meaningful_stemmed = meaningful_words #[stemmer.stem(w) for w in meaningful_words]
    return(" ".join(meaningful_stemmed))


def sentiment(text):

    processed_text = text #[review_to_words(text)]

    sentiment = joblib.load("svm3class.pkl")

    sentiment =  (sentiment.predict(processed_text))

    return sentiment