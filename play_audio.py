import os

def play(filename):
    os.system("aplay " + filename)

if __name__ == "__main__":
    play("audio_library/howcanIhelpyou.wav")
