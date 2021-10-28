#!/usr/bin/env python3
# Speak lines for an event
# By Alex Glow, for F3NR1R companion bot, on Hackster.io: bit.ly/f3nr1r

import serial
import time
import os

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    ser.write(b"sEarsUp\n")
    ser.write(b"sEarsDown\n")
    time.sleep(1)

    ser.write(b"sEarsUp\n")
    os.system("mpg123 ~/Documents/voicefiles/1-amcompbot.mp3")
    ser.write(b"sHeadLeft\n")
    os.system("mpg123 ~/Documents/voicefiles/2-design-fennec.mp3")
    ser.write(b"sHeadCenter\n")
    os.system("mpg123 ~/Documents/voicefiles/3-wiseowl.mp3")
    os.system("mpg123 ~/Documents/voicefiles/4-upgrades.mp3")
    ser.write(b"sHeadRight\n")
    ser.write(b"sEarsDown\n")
    time.sleep(0.5)
    ser.write(b"sEarsUp\n")