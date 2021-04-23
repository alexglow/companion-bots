#!/usr/bin/env python3
# Send high-level random movement commands to Teensy over serial
# By Alex Glow, for F3NR1R companion bot, on Hackster.io: bit.ly/f3nr1r

import serial
import time
import os
import random

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    ser.write(b"sEarsUp\n")

    while True:
        randsleep = random.randint(0, 4) # outputs 1-4
        randEars = random.randint(0,4)

        if randEars == 1:
            ser.write(b"sEarsUp\n")
        elif randEars == 2:
            ser.write(b"sEarsDown\n")
        else:
            time.sleep(.5)

        ser.write(b"sHeadRandom\n")
        time.sleep(randsleep)