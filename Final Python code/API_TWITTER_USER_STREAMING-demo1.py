from tweepy.streaming import StreamListener
from tweepy import Stream
import tweepy
import twitter_credentials
import json
import nltk
import re

jsonfile = 'twitter_user1.json'
locationfile = 'location.json'

with open(locationfile,'r') as lf:
    location_listSA3 = json.load(lf)


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
        if status.user.location is not None:
            location = nltk.word_tokenize(status.user.location)
            location = [word for word in location if word.isalpha()]
            for token in location:
                for i in range(len(location_listSA3)):
                    if re.match(token,location_listSA3[i]):
                        sentiment_tweet_dict['user'] = status.user.id
                        sentiment_tweet_dict['location'] = location_listSA3[i]
                        write_in(sentiment_tweet_dict)
                        break
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == "__main__":
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN_KEY, twitter_credentials.ACCESS_TOKEN_SECRET)
    Stream = Stream(auth, listener)
    Stream.filter(locations=[144.1616,-38.4941,144.94165,-37.4025])


