from twython import Twython, TwythonError
from sentiment.sentiment_module import sentiment
import pprint
#import time
#import numpy as np

def twitter(query):

    ckey = '9ctXbOOJnEtjc94F0BWIVcIIX'
    csecret = 'W3LKMIknqysVEljB1FRhGu7JT2faXGnZEb6lNeOGfBrQwoJXMk'
    atoken = '234546366-daFnZo785QUAuKfDxkkoXJeECgSh2Mjhiq3QQm2u'
    asecret = 'S72dud7GQZmEBXLGMWmGPIH9hMcwCutW3FIck8QtWZZPl'


    twitter = Twython(ckey, csecret, atoken, asecret)

    try:
        search_results = twitter.search(q=query, languages = ['pt'] ,count=100)
    except TwythonError as e:
        print (e)

    reviews = []

    tweets = []



    for tweet in search_results['statuses']:
        if tweet['lang'].encode("utf-8") == 'pt':
            tweets.append(tweet['text'])

    if tweets == []:
        return [], [], []

    sents = sentiment(tweets)
    both = zip(tweets,sents)
    overall_sentiment = []
    count_pos = 0
    count_neutral = 0
    count_neg = 0
    for i in range(len(both)):
        sent_dict = {}
        sent_dict['tweet'] = both[i][0]
        sent_dict['sentimento'] = both[i][1]
        if sent_dict['sentimento'] == 0:
            sent_dict['sentimento'] = "negative"
            overall_sentiment.append(-1.0)
            count_neg = count_neg + 1
        elif sent_dict['sentimento'] == 1:
            sent_dict['sentimento'] = "neutral"
            overall_sentiment.append(0.0)
            count_neutral = count_neutral + 1
        elif sent_dict['sentimento'] == 2:
            sent_dict['sentimento'] = "positive"
            overall_sentiment.append(1.0)
            count_pos = count_pos + 1

        reviews.append(sent_dict)

    overall_sentiment = sum(overall_sentiment)/len(overall_sentiment)
    #data = [{"Sentimento": "Negativo", "Tweets": count_neg},
    #        {"Sentimento": "Neutro", "Tweets": count_neutral},
    #        {"Sentimento": "Positvo", "Tweets": count_pos}]
    data = [count_neg, count_neutral, count_pos]
    return reviews, overall_sentiment, data

if __name__ == '__main__':
    pprint.pprint(twitter('dilma'))