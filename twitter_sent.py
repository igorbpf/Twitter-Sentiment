from twython import Twython, TwythonError
from sentiment.sentiment_module import sentiment
import pprint

def twitter(query):

    ckey = '9ctXbOOJnEtjc94F0BWIVcIIX'
    csecret = 'W3LKMIknqysVEljB1FRhGu7JT2faXGnZEb6lNeOGfBrQwoJXMk'
    atoken = '234546366-daFnZo785QUAuKfDxkkoXJeECgSh2Mjhiq3QQm2u'
    asecret = 'S72dud7GQZmEBXLGMWmGPIH9hMcwCutW3FIck8QtWZZPl'


    # Requires Authentication as of Twitter API v1.1
    #twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    twitter = Twython(ckey, csecret, atoken, asecret)

    try:
        search_results = twitter.search(q=query, languages = ['pt'] ,count=100)
    except TwythonError as e:
        print (e)



    reviews = []


    for tweet in search_results['statuses']:
        if tweet['lang'].encode("utf-8") == 'pt':
            sent_dict = {}
            sent = sentiment(tweet['text']) #.encode('utf-8'))
            rev = tweet['text'].encode('utf-8')
            sent_dict['review'] = rev
            sent_dict['sentiment'] = sent
            reviews.append(sent_dict)

    return reviews

if __name__ == '__main__':
    pprint.pprint(twitter('cristo redentor'))