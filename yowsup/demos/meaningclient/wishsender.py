import time

def sendwish( messageBody ):
    file = open('../lastwished.txt', 'r')
    today = time.strftime("%x")
    if file.readline().strip() == today:
    file.close()
    file = open('../lastwished.txt', 'w')
    file.write(today)
    file.close()
