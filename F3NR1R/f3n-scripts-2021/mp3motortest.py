#!/usr/bin/env python3
# Test controlling motors and playing MP3s simultaneously
# By Alex Glow, for F3NR1R companion bot, on Hackster.io: bit.ly/f3nr1r

import serial
import time
import os

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    ser.write(b"sEarsUp\n")
    ser.write(b"sEarsDown\n")
    time.sleep(2)

    ser.write(b"sEarsUp\n")
    os.system("mpg123 ~/Documents/voicefiles/hiimfenrir.mp3")
    time.sleep(1)
    os.system("mpg123 ~/Documents/voicefiles/firstrobotvoice.mp3")