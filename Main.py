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


if __name__ == '__main__':
	scriptpath = os.path.dirname(__file__)
	
	
	bots = [xkcd.bot(scriptpath), smbc.bot(scriptpath)]
	
	while(True):
		newDelay = 1314000	# Just assign it something ridiculously high (this is a year)
		for bot in bots:
			if bot.remainingdelay == 0:
				bot.fetch()
			newDelay = getMin(bot.remainingdelay, newDelay)
		
		for bot in bots:
			bot.remainingdelay = bot.remainingdelay - newDelay
		time.sleep(newDelay)
		
		