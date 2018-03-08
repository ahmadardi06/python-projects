#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

#while True:
GPIO.output(17, 1)
time.sleep(1)
GPIO.output(27, 1)
time.sleep(1)
GPIO.output(22, 1)
time.sleep(1)
