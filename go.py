#######################################
# go.py is the entrance to launch the whole functionality.
#######################################
import threading
import time
import distance as dis
import temperature as tpt
import speechtotext as stt
from library import *

# For monitoring the surrounding environment from various perspectives at the same time, we used multi-threading codes to achieve this goal. Each thread is responsible for a specific function.
threads = []

t1 = threading.Thread(target=dis.distance_func)
t2 = threading.Thread(target=tpt.temperature_func)
t3 = threading.Thread(target=stt.assistant)

threads.append(t1)
threads.append(t2)
threads.append(t3)
t1.start()
t2.start()
t3.start()
