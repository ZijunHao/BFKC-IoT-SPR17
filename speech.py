# coding=utf-8
import json
import wave
import time
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import TextToSpeechV1
import record_audio as ra
import play_audio as pa
import photo_module as pm
from library import *

# **** Hide personal information for privacy concern
speech_to_text = SpeechToTextV1(
    username='eaf1****-****-****-****-********db5e',
    password='************',
    x_watson_learning_opt_out=False
)
text_to_speech = TextToSpeechV1(
    username='5441****-****-****-****-********e674',
    password='************',
    x_watson_learning_opt_out=True)

# Set the port number for buzzer
buzzer = 8

def main():
    assistant()


def assistant():
    name = texttospeech('how can I help you')

    # Play audio "How can I help you?" in user's earphone
    pa.play(name)

    # Let the user record his/her input voice
    filename = ra.record()

    # Recognize and translate the user's input speech to text using IBM Bluemix NLP service
    speech2=speechtotext(filename)

    # speech2[0] returns the confidence of the text
    # speech2[1] returns the text content
    # We assume that when confidence > 0.25, the user records effective audio
    if Speech2[0] > 0.25:
        # i\If the user wants to set timer
        if "time" in speech2[1]:
            texttospeech('how many minutes')
            pa.play('output.wav')
            filename = ra.record()
            speech2=speechtotext(filename)
            if speech2[0] > 0.25:
                settime = int(speech2[1])
                set_timer(settime)
            else:
                texttospeech('Sorry I do not understand')
                pa.play('output.wav')

        # If the user wants to check the doneness of the food
        elif 'check' in speech2[1]:
            doneness = pm.well_done()
            texttospeech(doneness)
            pa.play('output.wav')

        # If the user wants to recognize the food
        elif 'recognize' in speech2[1]:
            tmp = 'The labels for this object are'
            label_list = pm.what_is_it()
            for label in label_list:
                tmp = tmp + str(label)
            texttospeech(tmp)
            pa.play('output.wav')

        # We ignore all other kinds of input speech
        else:
            texttospeech('Sorry I do not understand')
            pa.play('output.wav')

    # The confidence value is too low, we ignore this input
    else:
        texttospeech('Sorry I do not understand')
        pa.play('output.wav')
        time.sleep(30)


# This is the function used to set a timer (minutes)
def set_timer(settime):
    mins = 0
    timer = settime
    while mins != timer:
        time.sleep(60)
        mins += 1

    # When time is up, the buzzer will sound
    digitalWrite(buzzer,1)
    time.sleep(3)
    digitalWrite(buzzer,0)

    # When time is up, play "time up!" audio in user's earphone
    name = texttospeech('time up')
    pa.play(name)


# This is the function used to recognize and translate user's input speech into text through IBM Bluemix NLP library
def speechtotext(audio):
    try:
        with open(join(dirname(__file__), audio),
              'rb') as audio_file:
            result = speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=True,
            word_confidence=True, continuous=True, model="en-US_NarrowbandModel")
    except Exception as e:
        print e

    confidence = result['results'][0]['alternatives'][0]['confidence']
    transcript = result['results'][0]['alternatives'][0]['transcript']
    return [confidence,transcript]


# This is the function used to transform text into corresponding speech through IBM Bluemix NLP library
def texttospeech(text):
    with open(join(dirname(__file__), 'output.wav'),
          'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(text, accept='audio/wav',
                                  voice="en-US_AllisonVoice"))


if __name__ =="__main__":
    main()

