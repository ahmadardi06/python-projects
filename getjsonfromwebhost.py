#!/usr/bin/python
import RPi.GPIO as GPIO
import json, urllib, time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

#url = "http://apisendiri.000webhostapp.com/remote/status.php"
url = "http://apisendiri.000webhostapp.com/lampu/api.php"

while True:
 output = json.load(urllib.urlopen(url))
 val = int(output['value'])
 print "Status: ", output['value']
 GPIO.output(17, val)
 time.sleep(3)
