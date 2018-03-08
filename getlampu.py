#!/usr/bin/python

import json, urllib, time
import RPi.GPIO as GPIO

GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

#GPIO.output(4, True)
#GPIO.output(17, True)
#GPIO.output(27, True)
#GPIO.output(22, True)

while True:
 url = "http://apisendiri.000webhostapp.com/lampu/api.php"
 output = json.load(urllib.urlopen(url))
 #print "value: ", output['value']
 #print "code: ", output['code']

 if output['value'] == '1':
  GPIO.output(4, False)
  GPIO.output(17, True)
  GPIO.output(27, True)
  GPIO.output(22, True)
 elif output['value'] == '2':
  GPIO.output(4, True)
  GPIO.output(17, False)
  GPIO.output(27, True)
  GPIO.output(22, True)
 elif output['value'] == '3':
  GPIO.output(4, True)
  GPIO.output(17, True)
  GPIO.output(27, False)
  GPIO.output(22, True)
 else:
  GPIO.output(4, True)
  GPIO.output(17, True)
  GPIO.output(27, True)
  GPIO.output(22, False)
 time.sleep(3) 
