#  -*- coding: utf-8 -*-

from robots.text import robot as text_robot
from robots.user_input import *

content = {}

def start():

	content["searchTerm"] = askAndReturnSearchTerm()	
	content["prefix"] = askAndReturnPrefix()	
	content = text_robot(content)	
	

	print(content)

start()