import subprocess
import sys
import logging
import os
import platform

#os.chdir('/Users/indiana/python-test')
pcwd = os.getcwd()+os.sep+'mylog.txt'
oper_system = platform.system()

logging.basicConfig(filename=pcwd,format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',level=logging.DEBUG)
logging.info('The operating system is: '+oper_system)
logging.info(pcwd)
logging.info('The directory has changed.')

arg_sum = len(sys.argv)
try:
	farg = str(sys.arg[1])
except:
	logging.info("Argument is missing.")
	exit(1)

logging.info('Checking if process' + farg + ' is running.')

is_running = subprocess.call(['ps','-C',farg])
if is_running == 1:
	logging.warning = "System '+farg+' is not running."
	logging.info = "Start the +farg+' immediately."
	restart_farg = subprocess.call(['sudo','ps','-ef'])
	if restart_farg == 1:
		logging.error("Unable to start %s please check the logs." %farg)
	else:
		logging.info("%s succesfully started." %farg)
