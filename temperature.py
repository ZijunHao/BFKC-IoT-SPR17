import time
from library import *

# Set port numbers for temperature sensor and buzzer
sensor = 0
buzzer = 8

# This is the function used to detect the surrounding temperature
def temperature_func():
    digitalWrite(buzzer,0)
    while True:
        try:
            time.sleep(1)
            # Read the temperature value from the sensor
            temperature = temp(sensor,'1.1')
            if (temperature > 60.0):      # Set the threshold as 60 centigrade
                # The buzzer will sound when reaching the threshold
                digitalWrite(buzzer,1)
                time.sleep(1.5)
                digitalWrite(buzzer,0)
            elif (temperature < 0):       # Pass abnormal output
                pass
        except Exception as e:
            print e
            pass

if __name__ == "__main__":
    temperature_func()
