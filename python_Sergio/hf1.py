from datetime import datetime
import time
import random

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 
        27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 
        51, 53, 55, 57, 59]
number = 99

for i in range(5):
    rightThisMinute = datetime.today().minute
#Verifica si el minuto es impar (comparándolo en el array odds)
    if rightThisMinute in odds:
        print("This minute seems a little odd", number)
    else:
        print("Not an odd minute", number)
# waitTime = random.randint(1, 60)
# time.sleep(waitTime)