#!/usr/bin/env python

import ZeroSeg.led as led
import time
import random
from datetime import datetime

def date(device, deviceId):

    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year - 2000

    # Set day
    device.letter(deviceId, 8, int(day / 10))     # Tens
    device.letter(deviceId, 7, day % 10)          # Ones
    device.letter(deviceId, 6, '-')               # dash
    # Set day
    device.letter(deviceId, 5, int(month / 10))     # Tens
    device.letter(deviceId, 4, month % 10)     # Ones
    device.letter(deviceId, 3, '-')               # dash
    # Set day
    device.letter(deviceId, 2, int(year / 10))     # Tens
    device.letter(deviceId, 1, year % 10)     # Ones

def clock(device, deviceId, seconds):

    for _ in xrange(seconds):
    		hour = now.hour
		minute = now.minute
		second = now.second
		dot = second % 2 == 0
		# Set hours
		device.letter(1, 8, int(hour / 10))     # Tens
		device.letter(1, 7, hour % 10)     # Ones
		device.letter(1, 6, " ", 1)
		# Set minutes
		device.letter(1, 5, int(minute / 10))   # Tens
		device.letter(1, 4, minute % 10)        # Ones
		device.letter(1, 3, " ", 1)
		# Set seconds
		device.letter(1, 2, int(second / 10))   # Tens
		device.letter(1, 1, second % 10) # Ones

device = led.sevensegment()

while True:
    date(device, 0)
    time.sleep(5)
    device.clear()
    clock(device, 0, seconds=120)
device.clear()
