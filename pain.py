import keyboard
from threading import Timer
import time
import re
import pyaudio
from playsound import playsound
threshold = 4 # Number of ctrl presses per second to activate

capture = []

def parseSpam():
    str = ''.join(capture) # Make a string out of the array
    regex = re.compile(r'(True)+|(False)+') # Make the variable 'regex' a regex
    strrearr = regex.findall(str) # Match the string against the regex and return all matches in an array
    count = len(strrearr) / 2 # Divide by 2 because the array also contains key up events
    if(count >= threshold): # Check if key was pressed more than the threshold
        playsound('mine.wav') # Play sound

while True: # Main loop
    if(len(capture) == 0 and keyboard.is_pressed('ctrl')):
        capture.append("True") # First capture
    if(len(capture) >= 1 and len(capture) << 20): # This pushes the key state
        if keyboard.is_pressed('ctrl'):
            capture.append("True")
        else:
            capture.append("False")
    if(len(capture) == 20):
        parseSpam() # Check if key was pressed more than the threshold
        capture = [] # Reset the capture array
    time.sleep(0.05) # Delay between captures