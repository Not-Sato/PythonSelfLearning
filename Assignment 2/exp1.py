import schedule
import time
from plyer import notification
 
 
def send_break_alert(title, message):
    notification.notify(title=title, message=message, timeout=5)
 
 
schedule.every(10).seconds.do(send_break_alert, "Hydration Alert", "Time to drink some water!")
schedule.every(20).seconds.do(send_break_alert, "Posture Check", "Sit straight and relax your shoulders.")
 
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Reminder stopped. Take care!")