'''
Every comicbot needs this:
self.delay	# This determines the inerval, at which a check for a new comic happens (in seconds)
self.remainingdelay	# This variable is used for asynchronous timing of all the comics

def fetch(self)	# this function checks if there's a new comic and fetches it
def post(self)	# if there's a new comic, post it on the forums
'''

__all__ = ["xkcd", "smbc"]

