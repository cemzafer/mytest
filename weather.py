#!/usr/bin/env python
import os
import sys
import requests
import json

ankara_city_id = '323786'
istanbul_city_id = '745044'
apikey = 'db50a9a03603e804f25a1316d63407a4'
fname = os.getcwd() + os.sep + 'pagereq.json'
#print(fname)

try:
	city_par = str(sys.argv[1])
	if city_par == 'istanbul':
		city_id = istanbul_city_id
	elif city_par == 'ankara':
		city_id = ankara_city_id
	webpage = 'http://api.openweathermap.org/data/2.5/weather?id='+city_id+'&APPID='+apikey
except:
	if len(sys.argv)<2:
		print('Usage: {} <city>'.format(os.path.basename(sys.argv[0])))
	exit(100)

try:
	req = requests.get(webpage)
except:
	print('Check internet connection. Connection is lost.')
	exit(200)
else:
	fh = open(fname,'w')
	fh.write(req.text.encode('utf-8'))
	fh.close()
	
	json_file = open(fname,'r')
	json_data  = json.load(json_file)
	temp = float(json_data['main']['temp'])
	temp_k = temp - 273.15
	coord_lon = float(json_data['coord']['lon'])
	coord_lat = float(json_data['coord']['lat'])
	desc = json_data['weather'][0]['description']

	print('Ankara Sicaklik: {0}'.format(str(temp_k)))
	print('Koordinat: {0},{1}'.format(str(coord_lon), str(coord_lat)))
	print('Durum: {}'.format(desc))
