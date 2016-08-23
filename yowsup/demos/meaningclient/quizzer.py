import requests
import json
import ConfigParser
from random import randint
import pyodbc

def startQuiz(groupId):
    if(isQuizActive(groupId) == True):
        return False;
    else:
        #create a quiz
        print ('creating a quiz');
        conn = getDBConnection();
        cursor = conn.cursor()  
        cursor.execute("INSERT QuizState (groupId, isActive, questionCount, currentAnswer) OUTPUT INSERTED.qId VALUES (groupId, 1, 0, '')");
        print ('quiz created');
        conn.close();
        return True;

def getQuestion(groupdId):
    num1 = randint(9,99)
    num2 = randint(9,99)
    ans = num1 + num2
    question = num1 + "+" + num2
    #update current answer in db
    activeQId = getActiveQId(groupId);
    conn = getDBConnection();
    cursor = conn.cursor()
    cursor.execute("Update QuizState SET currentAnswer = ans WHERE groupId = groupId AND isActive = 1"); 
    conn.close();
    print ('updating answer');
    return question;

def isQuizActive(groupId):
    #check if a quiz is active against the db
    conn = getDBConnection();
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM QuizState WHERE groupId = groupId AND isActive = 1");
    numrows = int(cursor.rowcount)
    conn.close();
    if(numrows > 0):
        return True;
    else:
        return False

def getCurrentAnswer(groupId):
    #check the db for the current answer against the db and return
    conn = getDBConnection();
    cursor = conn.cursor()
    cursor.execute("SELECT currentAnswer FROM QuizState WHERE groupId = groupId AND isActive = 1");
    row = cursor.fetchone();
    conn.close();
    return row[0];

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
    conn = getDBConnection();
    cursor = conn.cursor();
    cursor.execute("UPDATE QuizState SET isActive = 0 WHERE groupId = groupId");
    conn.close();
    return "The quiz is over. The winner is x. The standings are.."

def wasLastQuestion(groupId):
    return False;

def getDBConnection():
    configParser = ConfigParser.RawConfigParser()   
    configFilePath = r'../apiconfigs.txt'
    configParser.read(configFilePath)
    server = configParser.get('quizdb', 'server')
    user = configParser.get('quizdb', 'user')
    password = configParser.get('quizdb', 'password')
    database = configParser.get('quizdb', 'database')
    conn = pymssql.connect(server=server, user=user, password=password, database=database);
    return conn;



