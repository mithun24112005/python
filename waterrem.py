import time
from plyer import notification
while True:
    notification.notify(
        title="***please drink water now!!!***",
        message="The National Academies of Science, Engineering and Medicine recommends the following for daily fluid intake: 125 ounces (3.7 liters) for men.",
        app_icon="D:\python\icon.ico", 
        timeout=10
    )
    time.sleep(60*60)