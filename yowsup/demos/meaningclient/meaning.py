import requests
import json

def getmeaningfromapi( messageBody ):
    word = messageBody.lower().replace("meaning?", "").strip()
    url = 'https://wordsapiv1.p.mashape.com/words/' + word
    headers = {"X-Mashape-Key": "mUFkRnNzzkmshprtCzJabFXeypDgp1tI7vZjsnPFdzXVL7buZx",
               "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return formatresponse(response.text, word)

def formatresponse(jsonstr, word):
    if word.lower() == "ramraj":
        formattedstr = "*ramraj*\n"
        formattedstr = formattedstr + "1. Given name for Ashwin Rao G by his grandmother. Later it was chagned to Ashwin as he thought it was not cool."
        return formattedstr;
    try:
        parsed_json = json.loads(jsonstr)
        formattedstr = "*" + word + "*\n"
        synonyms = ""
        i = 1
        for result in parsed_json['results']:
            formattedstr = formattedstr + str(i) + ". " + result['definition'] + "\n"
            try:
                for synonym in result['synonyms']:
                    synonyms = synonyms + synonym + ", "
            except:
                print ("Error while trying to get synonym")
            i=i+1
        return formattedstr + "\n" + "*Synonyms:* " + synonyms[:-2]
    except:
        return "*" + word + "* not found in dictionary"
