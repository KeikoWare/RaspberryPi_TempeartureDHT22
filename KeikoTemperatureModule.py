#!/usr/bin/python
import sys

import Adafruit_DHT
import urllib
import urllib2

url = 'https://www.keikoware.dk/temp/capture.php'
sensor = Adafruit_DHT.AM2302
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) 

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    payload = {'sensor':'pi_temp_001','temperature':temperature,'humidity':humidity}
    request = urllib2.Request(url,data=urllib.urlencode(payload))
    request.add_header('Content-Type','application/x-www-form-urlencoded')
    response = urllib2.urlopen(request) 
    print response.read()
    print response.code
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
