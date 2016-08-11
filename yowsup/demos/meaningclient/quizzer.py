import requests
import json
import ConfigParser
from random import randint

def startQuiz(groupId):
    if(isQuizActive(groupId) == True):
        return False;
    else:
        #create a quiz
        return True;

def getQuestion():
    num1 = randint(9,99)
    num2 = randint(9,99)
    ans = num1 + num2
    question = num1 + "+" + num2
    #update current answer in db
    return question;

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

def getIntroMessage():
    return "Hi.. Welcome to whatsapp quiz. The quiz will begin in 30 seconds. Points only for the first correct response.."

def updateQuestionCount(groupId):
    #update the question count
    return True;

def getFinalMessage(groupId):
    #close the quiz
    return "The quiz is over. The winner is x. The standings are.."

def wasLastQuestion(groupId):
    return False;


