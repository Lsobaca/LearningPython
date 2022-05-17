# Exercise 1: Change either the www.pythonlearn.com/code3/geojson.py or
# www.pythonlearn.com/code3/geoxml.py to print out the two-character country
# code from the retrieved data. Add error checking so your program does not
# traceback if the country code is not there. Once you have it working, search
# for “Atlantic Ocean” and make sure it can handle locations that are not in any
# country
from ctypes import addressof
import urllib.request,urllib.parse,urllib.error
import json

serviceURL = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    url = serviceURL + urllib.parse.urlencode({'sensor': 'false','address': address})
    
    print('Retrieving',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')
    
    try:
        js = json.loads(data)
    except BaseException:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure To Retrieve')
        print(data)
        continue
    
    counter = -1
    info = js['results'][0]['address_components']
    for item in info:
        counter += 1
        if js['results'][0]['address_components'][counter]['types'] == ['country','political']:
            print(js['results'][0]['address_component'][counter]['short_name'])
            break
        else:
            continue
    print("No country code")
    
    