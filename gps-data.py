import serial
import math

def konvert(dd):
 num = abs(dd)
 d = float(math.floor(num))
 m = num - d
 sign = '-' if dd < 0 else ''
 return sign + '%03i%02.5f' % (int(d), m * 60.00)

ser = serial.Serial('/dev/ttyS0', 9600,timeout=1)

x = ser.read(1200)
pos1 = x.find("$GPRMC")
pos2 = x.find("\n", pos1)
loc  = x[pos1:pos2]
data = loc.split(',')
if data[2] == 'V':
 print 'No location found'
else:
 print "Latitude =" + data[3]
 print "Longitude =" + data[5]
