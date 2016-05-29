import requests
import json
from application_only_auth import Client


def gettweetsfromapi( messageBody ):
    print ("I was here...")
    CONSUMER_KEY = getconsumerkey()
    CONSUMER_SECRET = getconsumersecret()
    print (CONSUMER_KEY)
    print (CONSUMER_SECRET)

    client = Client(CONSUMER_KEY, CONSUMER_SECRET)

    tweet = client.request('https://api.twitter.com/1.1/search/tweets.json?q=%23IPLfinal&count=5')
    print json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ':'))

    status = client.rate_limit_status()
    print status['resources']['search']

    #try:
    
    parsed_json = tweet
    formattedstr = ""
    print ("Json loaded")
    i = 1
    for status in parsed_json['statuses']:
        name = status['user']['screen_name']
        print (name)
        message = status['text']
        print (message)
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
    
