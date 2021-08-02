from plyer import notification

def NotifyMe(Message):
    notification.notify(
        title="Time to learn!",
        message = Message,
        timeout = 5,
        app_icon = "E:\\Python\\codes\\Learnig\\book1080.ico"
    )

NotifyMe('test')