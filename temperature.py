import time
from library import *

sensor = 0
buzzer = 8

def temperature_func():
    digitalWrite(buzzer,0)
    while True:
        try:
            time.sleep(1)
            temperature = temp(sensor,'1.1')
            if (temperature > 60.0):      #set the threshold as 60 centigrade
                digitalWrite(buzzer,1)
                time.sleep(1.5)
                digitalWrite(buzzer,0)
            elif (temperature < 0):       #pass abnormal output
                pass
        except Exception as e:
            print e
            pass

if __name__ == "__main__":
    temperature_func()
