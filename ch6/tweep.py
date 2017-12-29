import os
import tweepy
from pprint import pprint as pp

consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']

access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def _get_media_url(self, media):
        if not media:
            return []

        return [m['media_url_https'] for m in media if m['type'] == 'photo']

    def on_status(self, tweet):
        container = tweet._json

        entities = container.get('entities', {}).get('media')
        extended_entities = container.get('extended_entities', {}).get('media')
        extended_tweet = container.get('extended_tweet', {}).get('entities', {}).get('media')

        all_urls = set()
        for media in (entities, extended_entities, extended_tweet):
            urls = self._get_media_url(media)
            all_urls.update(set(urls))

        print
        print tweet.text
        for url in all_urls:
            print url


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
try:
    myStream.filter(track=['#dog', '#dogs', '#puppy', '#cat', '#kitty', '#lolcat', '#badkitty'])
except:
    pass