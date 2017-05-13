import os

# This is the function used to play the audio file. The input parameter is the path the audio file.
def play(filename):
    os.system("aplay " + filename)

if __name__ == "__main__":
    play("audio_library/howcanIhelpyou.wav")
