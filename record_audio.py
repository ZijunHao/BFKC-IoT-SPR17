import os
import signal
import time
import subprocess, threading
from datetime import datetime

def record():
    # Load audio module
    os.system("sudo modprobe snd_bcm2835")

    # Set command to record audio
    filename = "audio_library/%s.wav".format(datetime.now())
    command = "arecord -D plughw:1,0 " + filename
    pro = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

    # Set 5-second time slot for users to record their audio inputs
    time.sleep(5)
    pro.terminate()

    return filename


if __name__ == "__main__":
    record()
