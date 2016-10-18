#!/usr/bin/python

import re

mylist = []
avalue = ''

fh = open('/etc/passwd','r')

for k in fh:
	avalue = re.match(r'root',k,re.M|re.I)
	if avalue:
		print(k)
		mylist.append(k)

svalue = mylist[0].split(':')
print(svalue[4])

fh.close()

