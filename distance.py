import time
from library import *

ultrasonic_ranger = 4
buzzer = 8

def distance_func():
    while True:
        try:
            distance = ultrasonicRead(ultrasonic_ranger)
            print distance
            if (distance < 2.5):         #set the threshold as 2.5cm
                digitalWrite(buzzer,1)
                time.sleep(2)
                digitalWrite(buzzer,0)
            elif (distance > 100):       #pass abnormal output
                pass
        except Exception as e:
            print e

if __name__ == "__main__":
    distance_func()
