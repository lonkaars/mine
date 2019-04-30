import keyboard
from threading import Timer
import time
import re
import pyaudio
import wave
from playsound import playsound
threshold = 4 # number of ctrl presses per second to activate



def playMine():
    playsound('mine.wav')

capture = []

def parseSpam():
    str = ''.join(capture)

    regex = re.compile(r'(True)+|(False)+')
    strrearr = regex.findall(str)
    count = len(strrearr) / 2
    if(count >= threshold):
        playMine()

while True:
    if(len(capture) == 0 and keyboard.is_pressed('ctrl')):
        capture.append("True")

    if(len(capture) >= 1 and len(capture) << 20):
        if keyboard.is_pressed('ctrl'):
            capture.append("True")
        else:
            capture.append("False")

    if(len(capture) == 20):
        parseSpam()
        capture = []

    time.sleep(0.05)