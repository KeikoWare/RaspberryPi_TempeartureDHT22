#!/usr/bin/python
import sys

import Adafruit_DHT
import urllib
import urllib2

def getserial():
   # Extract serial from cpuinfo file
   cpuserial = "0000000000000000"
   try:
      f = open('/proc/cpuinfo','r')
      for line in f:
         if line[0:6]=='Serial':
            cpuserial = line[10:26]
      f.close()
   except:
      cpuserial = "test323456789"
   return cpuserial

url = 'https://www.keikoware.dk/temp/capture.php'
#sensor = Adafruit_DHT.AM2302
sensor = Adafruit_DHT.DHT22
pin = 4
uid = getserial()
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    payload = {'sensor':'pi_temp_001','uid':uid,'temperature':temperature,'humidity':humidity}
    request = urllib2.Request(url,data=urllib.urlencode(payload))
    request.add_header('Content-Type','application/x-www-form-urlencoded')
    response = urllib2.urlopen(request)
    print response.read()
    print response.code
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
