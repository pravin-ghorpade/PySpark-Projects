from kafka import KafkaProducer
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from transformers import pipeline
import json
import configparser


#Twitter API Authentication credentials
consumer_key = "ksPgyTZlVW4HxUPYHbaZcolbb"
consumer_secret = "FPqAlq81vTLaFUcmyw9z3Zu25x2dNB8R7cLEhifqVmjlVp4knH"
access_token = "3030322778-hDtBWvsKaUfFQGbbflArknfcSfm4HF9LPo7qtnq"
access_token_secret = "x6CP6USzNdYilsxvPBPJLhO3r7oHdIXNWHkfiMdxOQ6HN"



def perform_analysis(tweet):
	transformer_sentiment = classifier(json.loads(tweet)["text"])


	transformer_sentiment = transformer_sentiment[0]['label']

	return transformer_sentiment


# Twitter Stream Listener

class KafkaPushListener(tweepy.Stream):
    def __init__(self):
        # localhost:9092 = Default Zookeeper Producer Host and Port Adresses
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])



    def on_data(self, data):
        # Producer produces data for consumer
        # Data comes from Twitter
        transformer_sentiment = perform_analysis(data)
        self.producer.send(config['arguments']['topic'], transformer_sentiment.encode('utf-8'))
        return True

    def on_error(self, status):
        print("status error - ",status)
        return True



if __name__ == "__main__":


	# TWITTER API AUTH
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	config = configparser.ConfigParser()
	config.read('config.ini')


	# Search String to search on Twitter.
	search_text = config['arguments']['search_string']
	# search_text = "#olympics"

	classifier = pipeline('sentiment-analysis')


	listener = KafkaPushListener()
	twitter_stream = Stream(consumer_key, consumer_secret, access_token, access_token_secret)

	twitter_stream.filter(track=['#Covid19'])