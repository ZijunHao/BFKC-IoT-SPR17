import time
from library import *

#Set port numbers for ultrasonic sensor and buzzer
ultrasonic_ranger = 4
buzzer = 8

# This is the function used to measure the distance between people's finger and knife
def distance_func():
    while True:
        try:
            # Read the distance (centimeters) from ultrasonic sensor
            distance = ultrasonicRead(ultrasonic_ranger)
            print distance
            if (distance < 2.5):         #Set the threshold as 2.5cm
                # The buzzer will sound when reaching the threshold
                digitalWrite(buzzer,1)
                time.sleep(2)
                digitalWrite(buzzer,0)
            elif (distance > 100):       # Pass abnormal output
                pass
        except Exception as e:
            print e

if __name__ == "__main__":
    distance_func()
