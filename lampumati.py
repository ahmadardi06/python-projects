#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.output(4, 0)
GPIO.output(17, 0)
GPIO.output(27, 0)
