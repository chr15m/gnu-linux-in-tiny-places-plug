#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

ledpin = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.output(ledpin, GPIO.LOW)

try:
    for c in range(10000):
        GPIO.output(ledpin, GPIO.LOW if c %2 else GPIO.HIGH)
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
