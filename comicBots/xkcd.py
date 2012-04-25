'''
Created on 22.04.2012

@author: Lukas 'DrLuke' Jackowski
'''

class xkcd(object):
	'''
	classdocs
	'''


	def __init__(self):
		'''
		Constructor
		'''
		self.delay = 7
		self.remainingdelay = self.delay
	
	def fetch(self):
		self.remainingdelay = self.delay
		print("xkcd")
	
	def post(self):
		pass
	