'''
Created on 22.04.2012

@author: Lukas 'DrLuke' Jackowski
'''

import os, time

class bot(object):
	'''
	classdocs
	'''


	def __init__(self, scriptpath):
		'''
		Constructor
		'''
		self.delay = 7
		self.remainingdelay = 0
		self.debugfile = open(os.path.join("logs", scriptpath), "a", encoding="utf-8")
	
	def fetch(self):
		self.remainingdelay = self.delay
		print("xkcd")
	
	def post(self):
		pass
	