import os
import time
import serial
import string
import pynmea2
import urllib2
import requests
import urllib

while True:
 port = "/dev/ttyS0"
 ser = serial.Serial(port, baudrate=9600, timeout=0.5)
 dataout = pynmea2.NMEAStreamReader()
 newdata = ser.readline()

 print("Get Lat and Long")
 if newdata[0:6] == '$GPGGA':
  newmsg = pynmea2.parse(newdata)
  lat = newmsg.latitude
  print (lat)
  lng = newmsg.longitude
  print (lng)
  print lat,",",lng

  #URL = "http://172.20.10.7/latihan/insertlocation.php"
  #PARAMS = {'lat': lat, 'lng':lng}
  #method POST
  #req = requests.post(URL, data = PARAMS)
  #data = req.json()
  #print data['status']

  url = "http://ahmadardi06.it.student.pens.ac.id/lampu/uploadlocation.php?lat="+str(lat)+"&lng="+str(lng)
  f = requests.get(url)
  print f.json()
  
  #delay 20 detik
  time.sleep(20)
