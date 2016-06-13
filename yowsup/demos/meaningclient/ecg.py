import os
import time

def queueThisPerson( phone ):
    return queueCount(phone)

def queueCount( phone ):
    ecgfile = '../ecgqueue.txt'
    file = open(ecgfile, 'r')
    lines = file.read().splitlines()
    file.close()
    if phone in lines:
       return 'You are already in queue..'

    file = open(ecgfile, 'a')
    file.write(phone)
    file.write('\n')
    file.close()

    return 'You are ' + len(lines) + ' in queue..'

def dequeueEcg():
    ecgfile = '../ecgqueue.txt'
    file = open(ecgfile, 'r')
    lines = file.read().splitlines()
    file.close()
    firstGuy = lines.pop(0)
    t = time.time()
    os.rename(ecgfile, ecgfile + str(t))
    file = open(ecgfile, 'w')
    for item in lines:
        file.write("%s\n" % item)
    return firstGuy