#!/usr/bin/env python -tt

import sys
import os

def hello(name):
	name = name + '!!!'
	print('Hello ' + name)

def main():
	hello(sys.argv[1])

if __name__ == '__main__':
#print(len(sys.argv))
	try:
		main()
	except:
		print('Please use as '+os.path.basename(sys.argv[0])+' <name>')
