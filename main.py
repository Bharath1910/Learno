from plyer import notification
import pickle, random, time

Formulas = None
Time = None

def NotifyMe(Message):
    notification.notify(
        title="Time to learn!",
        message = Message,
        timeout = 5,
        app_icon = "E:\\Python\\codes\\Learnig\\book1080.ico"
    )

def WaitTime(Time_interval):
    Min = 60/int(Time_interval)
    sleeptime = 60*Min

    return int(sleeptime)

with open("E:\\Python\\codes\\Learnig\\config.bin","rb+") as f:
    a = pickle.load(f)
    Formulas = a["Formulas"] 
    Time = a["Time"] 

while True:
    NotifyMe(random.choice(Formulas))
    time.sleep(WaitTime(Time))
