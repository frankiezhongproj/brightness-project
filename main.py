import time
from datetime import datetime
import screen_brightness_control as screen_brightness


def fader(target, increment=1, wait=0.02):
   current_brightness = round(screen_brightness.get_brightness()[0])


   while current_brightness != target:
       if current_brightness > target:
           current_brightness = max(current_brightness - increment, target)
       else:
           current_brightness = min(current_brightness + increment, target)


       screen_brightness.set_brightness(int(current_brightness))
       time.sleep(wait)


def change_time(time_now):
   current = round(screen_brightness.get_brightness()[0])
   if 5 <= time_now < 12:
       if current != 100:
           fader(100)
   elif 12 <= time_now < 17:
       if current <= 85:
           pass
       else:
           fader(85)
   elif 17 <= time_now < 20:
       if current <= 70:
           pass
       else:
           fader(70)
   else:
       if current <= 50:
           pass
       else:
           fader(50)


while True:
   try:
       time_now = datetime.now().hour
       change_time(time_now)
   except Exception as e:
       print(e)
   time.sleep(15)

