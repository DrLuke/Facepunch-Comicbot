'''
Created on 22.04.2012

@author: Lukas 'DrLuke' Jackowski
'''

import urllib, urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import re, io, os, time, json

class bot(object):
	'''
	classdocs
	'''


	def __init__(self, scriptpath):
		'''
		Constructor
		'''
		self.delay = 3600
		self.remainingdelay = 0
		self.scriptpath = scriptpath
		self.debugfile = open(os.path.join(self.scriptpath, "logs", "xkcd"), "a")
		
		file = open(os.path.join(self.scriptpath, "prevcomic","xkcd"), "r", encoding="utf-8")
		self.prevcomic = file.read()
		file.close()
		
	
	def fetch(self):
		self.remainingdelay = self.delay
		
		
		try:
			xkcd = urllib.request.urlopen("http://xkcd.com/")
		except:
			self.debugfile.write("Couldn't access 'http://xkcd.com/'.\nAborting...")
		else:
			xkcd_content = xkcd.read()
			soup = BeautifulSoup(xkcd_content)
						# Get the title of the comic
			for item in soup.find_all(id="ctitle"):
				comictitle = item.get_text()
				
			# and then get the comic-url and it's caption
			for item in soup.find_all(id="comic"):
				comicurl = item.img.get("src")
				comiccaption = item.img.get("title")
				if item.a:
					comiclarge = item.a.get("href")
				else:
					comiclarge = None
				
			# Decode the page's content so it can be used with the regex search function
			xkcd_content_decoded = xkcd_content.decode("utf-8")
			# Search the permalink located on the site
			match = re.search(r'http://xkcd.com/?([^\< >]+)', xkcd_content_decoded )
			if match:
				origlink = match.group(0)
					
	
					
			if self.prevcomic == comictitle:
				pass
			elif self.prevcomic == "":
				file = open(os.path.join(self.scriptpath, "prevcomic","xkcd"), "w", encoding="utf-8")
				file.write(comictitle)
				self.prevcomic = comictitle
				file.close()
			else:
				self.post(comictitle, comicurl, comiccaption, origlink, comiclarge)
				pass
		
		
	
	def post(self, comictitle, comicurl, comiccaption, origlink, comiclarge):
		timestring = time.strftime("%a, %d %b %Y %H:%M:%S")
		self.debugfile.write("["+ timestring +"] Found new comic titled '" + comictitle + "'\n")
		self.debugfile.write("Attempting to post comic\n")
		

		urllib.request.urlopen("http://api.facepun.ch/?username=xkcd.com&password=25d55ad283aa400af464c76d713c07ad&action=authenticate")
		
		# Check if the comiclarge actually is a large version of the comic, or linking elsewhere
		
		if comiclarge == None:
			postcontent = "[b][url=" + origlink + "]" + comictitle + "[/url][/b]\n\n[img]" + comicurl + "[/img]\n\n[i]" + comiccaption + "[/i]"
		else:
			postcontent = "[b][url=" + origlink + "]" + comictitle + "[/url][/b]\n\n[url="+ comiclarge +"][img]" + comicurl + "[/img][/url]\n\n[i]" + comiccaption + "[/i]"
		
		# Encode it to utf8 format
		data = urllib.parse.urlencode({"thread_id": "1179406", "message":postcontent}).encode("utf-8")
		
		# Post the comic
		post = urllib.request.urlopen("http://api.facepun.ch/?username=xkcd.com&password=25d55ad283aa400af464c76d713c07ad&action=newreply",data)
		postreturn = post.read().decode("utf-8")
		postjsonobj = json.loads(postreturn)
		try:
			if postjsonobj["reply"] == "OK":
				self.debugfile.write("New comic posted succesfully\n")
				file = open(os.path.join(self.scriptpath, "prevcomic","xkcd"), "w", encoding="utf-8")
				file.write(comictitle)
				self.prevcomic = comictitle
				file.close()
			else:
				self.debugfile.write("Failed to post comic, will retry at next interval\n")
		except:
			self.debugfile.write("Failed to post comic, will retry at next interval\n")
		
		# Apply everything written to the debugfile
		self.debugfile.flush()