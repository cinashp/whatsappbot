import requests
import json
import ConfigParser

def getQuestion():
    #Create a math question, like randomNumber() + randomNumber() + randomNumber()
    question = "100 + 10"
    return question

def isQuizActive(groupId):
    #check if a quiz is active against the db
    return False

def getCurrentAnswer(groupId):
    #check the db for the current answer against the db and return
    return 1;

def updateScore(groupId, sender):
    #update score in the db
    return False;

def getScore(groupId):
    #get the score from db
    return "hi"


