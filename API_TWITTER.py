from tweepy.streaming import StreamListener
from tweepy import Stream
import tweepy
import twitter_credentials
import search_params

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN_KEY, twitter_credentials.ACCESS_TOKEN_SECRET)
    Stream = Stream(auth, listener)
    Stream.filter(locations=search_params.D5, languages=search_params.LANGUAGES, track=search_params.KEY_WORDS)
