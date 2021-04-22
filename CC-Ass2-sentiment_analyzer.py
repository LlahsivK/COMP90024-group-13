import re
import json
import nltk

from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

#Try with tiny Twitter. Small one takes about 20 mins!
twitter_file = 'smallTwitter.json'

outfile = 'revised_smallTwitter.json'

'''
Using NLTK sentiment analyzer
'''
tt = open(twitter_file,'r',encoding='utf-8').read()
twitter_data = json.loads(tt)


# Total number of tweets in file
number_of_tweets = len(twitter_data['rows']) 


sia = SentimentIntensityAnalyzer()

updated_tweets = []

for tweets in range(number_of_tweets):
    tweet = twitter_data["rows"][tweets]
    
    ##Process text file
    tweet_text = tweet["value"]["properties"]["text"].lower()
    
    sentiment_tweet_dict = {}

    sentiment_score = sia.polarity_scores(tweet_text)

    sentiment_score_compound = sentiment_score['compound']
    
    sentiment_tweet_dict['sentiment'] = sentiment_score

    if sentiment_score_compound == 0:
        overall_sentiment = 'neutral'
    elif sentiment_score_compound > 0:
        overall_sentiment = 'positive'
    else:
        overall_sentiment = 'negative'
    
    sentiment_tweet_dict['overall_sentiment'] = overall_sentiment
    
    tweet.update(sentiment_tweet_dict)
    
    updated_tweets.append(tweet)
    
revised_tweets = {}

revised_tweets['rows'] = updated_tweets

with open(outfile,'w') as jsonFile:
    json.dump(revised_tweets, jsonFile)