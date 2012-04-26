'''
Created on 22.04.2012

@author: Lukas 'DrLuke' Jackowski
'''

class bot(object):
	'''
	classdocs
	'''


	def __init__(self, scriptpath):
		'''
		Constructor
		'''
		self.delay = 10
		self.remainingdelay = 0
	
	def fetch(self):
		self.remainingdelay = self.delay
		print("smbc")
	
	def post(self):
		pass