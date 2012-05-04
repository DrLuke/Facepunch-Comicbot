'''
Created on 22.04.2012

@author: Lukas 'DrLuke' Jackowski
'''

import urllib, urllib.request, urllib.error, urllib.parse
import re, io, os, time
import json

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
		self.debugfile = open(os.path.join(self.scriptpath, "logs", "smbc"), "a")
		
		file = open(os.path.join(self.scriptpath, "prevcomic","smbc"), "r", encoding="utf-8")
		self.prevcomic = file.read()
		file.close()
	
	def fetch(self):
		self.remainingdelay = self.delay
		
		try:
			smbc = urllib.request.urlopen("http://www.smbc-comics.com")
		except:
			self.debugfile.write("Couldn't access 'http://smbc-comics.com/'.\nAborting...")
		else:
			smbc_content = smbc.read().decode("utf-8")
			
			comictitlematch = re.search(r"[0-9]+\.gif", smbc_content)	
			comictitle = comictitlematch.group(0)
			comicurl = "http://www.smbc-comics.com/comics/" + comictitle
			aftercomictitlematch = re.search(r"[0-9]+after\.gif", smbc_content)
			aftercomictitle = aftercomictitlematch.group(0)
			aftercomicurl = "http://www.smbc-comics.com/comics/" + aftercomictitle
			
			prevcomicmatch = re.search(r"id=[0-9]+\#comic", smbc_content)
			prevcomicidmatch = re.search(r"[0-9]+", prevcomicmatch.group(0))
			curcomicid = int(prevcomicidmatch.group(0)) + 1
			
			if comictitle == self.prevcomic:
				pass
			elif self.prevcomic == "":
				file = open(os.path.join(self.scriptpath, "prevcomic","xkcd"), "w", encoding="utf-8")
				file.write(comictitle)
				self.prevcomic = comictitle
				file.close()
			else:
				self.post(comictitle, curcomicid, comicurl, aftercomicurl)
			
			
	
	def post(self, comictitle, curcomicid, comicurl, aftercomicurl):
		timestring = time.strftime("%a, %d %b %Y %H:%M:%S")
		self.debugfile.write("["+ timestring +"] Found new comic titled '" + comictitle + "'\n")
		self.debugfile.write("Attempting to post comic\n")
		# Auth with the Facepunch API
		urllib.request.urlopen("http://api.facepun.ch?username=smbc%20comics&password=25d55ad283aa400af464c76d713c07ad&action=authenticate")
		# Generate the content of the post
		postcontent = "[b][url=http://www.smbc-comics.com/index.php?db=comics&id="+str(curcomicid)+"#comic]Link to original comic[/url][/b]\n\n[img]" + comicurl + "[/img]\n\n[img]" + aftercomicurl + "[/img]"
		# Encode it to utf8 format
		
		data = urllib.parse.urlencode({"thread_id": "1179406", "message":postcontent}).encode("utf-8")
	
		# Post the comic
		post = urllib.request.urlopen("http://api.facepun.ch/?username=smbc%20comics&password=25d55ad283aa400af464c76d713c07ad&action=newreply",data)
		postreturn = post.read().decode("utf-8")
		postjsonobj = json.loads(postreturn)
		try:
			if postjsonobj["reply"] == "OK":
				self.debugfile.write("New comic posted succesfully\n")
				file = open(os.path.join(self.scriptpath, "prevcomic","smbc"), "w", encoding="utf-8")
				file.write(comictitle)
				self.prevcomic = comictitle
				file.close()
			else:
				self.debugfile.write("Failed to post comic, will retry at next interval\n")
		except:
			self.debugfile.write("Failed to post comic, will retry at next interval\n")