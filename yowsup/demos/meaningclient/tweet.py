import requests
import json
import ConfigParser
from application_only_auth import Client


def gettweetsfromapi( messageBody ):
    CONSUMER_KEY = getconsumerkey()
    CONSUMER_SECRET = getconsumersecret()
    client = Client(CONSUMER_KEY, CONSUMER_SECRET)

    hashtag = gethashtag(messageBody);
    tweet = client.request('https://api.twitter.com/1.1/search/tweets.json?q=' + hashtag + '&count=5')

    status = client.rate_limit_status()
    print status['resources']['search']

    return formattweet(tweet)

def formattweet(tweet):
    try:
        parsed_json = tweet
        formattedstr = ""
        i = 1
        for status in parsed_json['statuses']:
            name = status['user']['screen_name']
            message = status['text']
            formattedstr = formattedstr + str(i) + ". *" + name + "*: "
            formattedstr = formattedstr + message + "\n\n"
            i=i+1
        return formattedstr
    except Exception, e:
        print e
        return "Unknown error occured while fetching the tweet..."


def gethashtag( messageBody ):
    hashtags = set([word[1:] for word in messageBody.split(' ') if word.startswith("#")])
    urlencodedhashtags = ""
    for hashtag in set(hashtags):
        urlencodedhashtags = urlencodedhashtags + "%23" + hashtag + "+"
    print (urlencodedhashtags[:-1])
    return urlencodedhashtags[:-1]

def getconsumerkey():
    configParser = ConfigParser.RawConfigParser()   
    configFilePath = r'../apiconfigs.txt'
    configParser.read(configFilePath)
    return configParser.get('twitter', 'consumerkey')

def getconsumersecret():
    configParser = ConfigParser.RawConfigParser()   
    configFilePath = r'../apiconfigs.txt'
    configParser.read(configFilePath)
    return configParser.get('twitter', 'consumersecret')
