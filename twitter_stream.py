from dotenv import load_dotenv
from pathlib import Path

import os

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')

KAFKA_HOST = os.getenv('KAFKA_HOST') or 'localhost'
KAFKA_PORT = os.getenv('KAFKA_PORT') or '9092'


class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages('paygap', data.encode('utf-8'))
        print(data)
        return True

    def on_error(self, status):
        print('Error fetching data from twitter. Status code: {}' \
            .format(status))

kafka = KafkaClient('{}:{}'.format(KAFKA_HOST, KAFKA_PORT))
producer = SimpleProducer(kafka)
listener = StdOutListener()

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
stream = Stream(auth, listener)

stream.filter(track='paygap', async=True)
