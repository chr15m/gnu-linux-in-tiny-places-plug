#!/usr/bin/env python

import RPi.GPIO as GPIO
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 10000))

ledpin = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.output(ledpin, GPIO.LOW)

try:
    c = 0
    while 1:
        data, address = sock.recvfrom(4096)
        c += 1
        GPIO.output(ledpin, GPIO.LOW if c %2 else GPIO.HIGH)
except KeyboardInterrupt:
    GPIO.cleanup()

