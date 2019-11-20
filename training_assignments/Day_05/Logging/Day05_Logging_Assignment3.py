'''
3. Write a program to check students percentage, accept percentage from user,
if percentage is >=80 log the debug message,
if percentage >=65 & <80 log info message,

if percentage >=50 & <65 log warning message,
if percentage >=35 & <50 log critical message,
and if percenage <35 log error message.


create two handlers(StreamHandler, FileHandler) and then send all log messages to StreanHandler and all error and critical messages to FileHandler and both handlers 
have different logging formats.and program will terminate only if percentage is <=0 or >100.

'''

import logging
import sys

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs.log')

stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_format)

file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

def check_percentage(percentage):
	if percentage >= 80:
		logger.debug("Student got Distinction")
	elif percentage >=65 and percentage < 80:
		logger.info("Student got First Class")
	elif percentage >= 50 and percentage <65:
		logger.warning("Student got Second Class")
	elif percentage >= 35 and percentage <50:
		logger.error("Student got Pass Class")
	elif percentage <35:
		logger.critical("Student is Failed")
if __name__=='__main__':
	
	while True:
		percentage = int(input("Enter percentage"))
		if(percentage<0 or percentage>100):
			sys.exit()
		check_percentage(percentage)