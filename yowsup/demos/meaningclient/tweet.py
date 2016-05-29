import requests
import json
from application_only_auth import Client


def gettweetsfromapi( messageBody ):
    CONSUMER_KEY = getconsumerkey()
    CONSUMER_SECRET = getconsumersecret()

    client = Client(CONSUMER_KEY, CONSUMER_SECRET)

    tweet = client.request('https://api.twitter.com/1.1/search/tweets.json?q=%23IPLfinal&count=5')

    status = client.rate_limit_status()
    print status['resources']['search']

    #try:
    
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
    #except:
    return "Unknown error occured..."

def getscorefromapi( messageBody ):
    CONSUMER_KEY = getconsumerkey()
    CONSUMER_SECRET = getconsumersecret()

    client = Client(CONSUMER_KEY, CONSUMER_SECRET)

    tweet = client.request('https://api.twitter.com/1.1/search/tweets.json?q=from:IPL&count=5')

    status = client.rate_limit_status()
    print status['resources']['search']

    #try:
    
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
    #except:
    return "Unknown error occured..."

def getconsumerkey():
    with open('../consumerkey.txt', 'r') as f:
        first_line = f.readline()
    return first_line.strip()

def getconsumersecret():
    with open('../consumersecret.txt', 'r') as f:
        first_line = f.readline()
    return first_line.strip()
    
