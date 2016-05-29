import requests
import json

def getmeaningfromapi( messageBody ):
    word = messageBody.lower().replace("meaning", "").strip()
    url = 'https://wordsapiv1.p.mashape.com/words/' + word
    headers = {"X-Mashape-Key": "mUFkRnNzzkmshprtCzJabFXeypDgp1tI7vZjsnPFdzXVL7buZx",
               "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return formatresponse(response.text, word)

def formatresponse(jsonstr, word):
    try:
        parsed_json = json.loads(jsonstr)
        formattedstr = "*" + word + "*\n"
        i = 1
        for result in parsed_json['results']:
            formattedstr = formattedstr + str(i) + ". " + result['definition'] + "\n"
            i=i+1
        return formattedstr
    except:
        return "*" + word + "* not found in dictionary"
