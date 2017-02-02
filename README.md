# Twitter-Sentiment
Web app which analyzes the sentiment of tweets of a specific theme (Portuguese only).

The dataset used for the training of the classifier was scrapped from tripadvior restaurants' reviews.

The classifier is saved in a .pkl file. It is the svm3class.pkl. It categorizes the tweets in POSITIVE, NEGATIVE and NEUTRAL.

svm2class.pkl it is not used, but it can classifiy tweets between POSITIVE and NEGATIVE only.


# Usage
Create a virtual environment and export variables, but first you need to go to Twitter api and get tokens and keys.

export consumer_key=CONSUMER_KEY
export consumer_token=CONSUMER_TOKEN
export access_token=ACCESS_TOKEN
export access_secret=ACCESS_SECRET

run python app.py
