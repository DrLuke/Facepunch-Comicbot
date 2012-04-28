'''
Created on 22.04.2012

@author: Lukas 'DrLuke' Jackowski
'''

import os, math, time, re, io

from comicBots import *

def getMin(a,b):
	'''
	return the smaller value of a pair
	'''
	if a < b:
		return a
	else:
		return b
	
def updategit():
	'''
	This Function runs a small shell script that checks if there's a new version of this script on git.
	If this is true, the shell script will terminate this script, update it, and run it again.
	'''
	pass


if __name__ == '__main__':
	scriptpath = os.path.dirname(__file__)
	
	
	bots = [xkcd.bot(scriptpath), smbc.bot(scriptpath)]
	
	while(True):
		updategit()
		newDelay = 1314000	# Just assign it something ridiculously high (this is a year)
		for bot in bots:
			if bot.remainingdelay == 0:
				bot.fetch()
			newDelay = getMin(bot.remainingdelay, newDelay)
		
		for bot in bots:
			bot.remainingdelay = bot.remainingdelay - newDelay
		time.sleep(newDelay)
		
		