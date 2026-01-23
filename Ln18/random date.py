import random
import time

def getRandomDate(startDATE,endDATE):
    print("A random date between",startDATE,"and",endDATE)
    randomGenerator =random.random()
    format='%m/%d/%Y'

    startTime=time.mktime(time.strptime(startDATE,format))
    endTime=time.mktime(time.strptime(endDATE,format))

    randomTime=startTime+ randomGenerator*(endTime-startTime)
    randomDate=time.strftime(format,time.localtime(randomTime))
    return randomDate
print("random date is",getRandomDate("1/1/2016","12/12/2018"))