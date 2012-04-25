'''
Created on 22.04.2012

@author: Lukas 'DrLuke' Jackowski
'''

class smbc(object):
	'''
	classdocs
	'''


	def __init__(self):
		'''
		Constructor
		'''
		self.delay = 10
		self.remainingdelay = self.delay
	
	def fetch(self):
		self.remainingdelay = self.delay
		print("smbc")
	
	def post(self):
		pass