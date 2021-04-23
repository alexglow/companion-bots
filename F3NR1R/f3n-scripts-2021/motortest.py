#!/usr/bin/env python3
# Test sending high-level movement commands to Teensy over serial
# By Alex Glow, for F3NR1R companion bot, on Hackster.io: bit.ly/f3nr1r

import serial
import time
import os

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    ser.write(b"sEarsUp\n")
    time.sleep(1)
    ser.write(b"sEarsDown\n")
    time.sleep(1)
    ser.write(b"sEarsUp\n")
    time.sleep(1)
    ser.write(b"sHeadLeft\n")
    time.sleep(1)
    ser.write(b"sHeadRight\n")