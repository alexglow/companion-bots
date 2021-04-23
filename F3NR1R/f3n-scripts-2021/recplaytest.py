#!/usr/bin/env python3
# Test recording audio and playing it back
# By Alex Glow, for F3NR1R companion bot, on Hackster.io: bit.ly/f3nr1r

import serial
import time
import os

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    ser.write(b"sEarsUp\n")
    os.system("echo 'Hey! How are you?' | festival --tts")

    ser.write(b"sEarsDown\n")
    os.system("arecord -d 3 testrec.wav")
    time.sleep(2)

    ser.write(b"sEarsUp\n")
    os.system("echo 'You said' | festival --tts")
    os.system("aplay testrec.wav")
    time.sleep(1)