from tweepy.streaming import StreamListener
from tweepy import Stream
import json
import tweepy
import twitter_credentials
from nltk.sentiment import SentimentIntensityAnalyzer

jsonfile = 'analyzed_twitter.json'
sia = SentimentIntensityAnalyzer()
update_list = []

with open(jsonfile, 'w') as jsonFile:
    json.dump(update_list, jsonFile)

def write_in(dic):
    with open(jsonfile,'r') as jf:
        update_list = json.load(jf)

    with open(jsonfile, mode='w') as jf:
        update_list.append(dic)
        json.dump(update_list,jf)


class StdOutListener(StreamListener):

    def on_status(self, status):
        sentiment_tweet_dict = {}
        tweet_text = status.text.lower()
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
        sentiment_tweet_dict['box coordinates'] = status.place.bounding_box.coordinates
        write_in(sentiment_tweet_dict)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == "__main__":
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN_KEY, twitter_credentials.ACCESS_TOKEN_SECRET)
    Stream = Stream(auth, listener)
    Stream.filter(locations=[144.4303,-37.994,145.5839,-37.4095])