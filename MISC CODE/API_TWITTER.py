from tweepy.streaming import StreamListener
from tweepy import Stream
import tweepy
import twitter_credentials

class StdOutListener(StreamListener):

    def on_status(self, status):
        print(status.text,status.place.bounding_box.coordinates)
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
