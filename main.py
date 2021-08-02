from notifi import NotifyMe
import pickle
import random
import time

Formulas = []

with open("E:\\Python\\codes\\Learnig\\config.bin","rb+") as f:
    a = pickle.load(f)
    Formulas, a = a, Formulas

Time = None

with open("E:\\Python\\codes\\Learnig\\config.txt",'r') as f:
    a = f.readline()
    Time,a = a,Time

def WaitTime(Time_interval):
    Min = 60/int(Time_interval)
    sleeptime = 60*Min

    return int(sleeptime)


while True:
    NotifyMe(random.choice(Formulas))
    time.sleep(WaitTime(Time))

