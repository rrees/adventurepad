from models import Adventure

from google.appengine.ext import db
from google.appengine.tools import bulkloader

class AdventureLoader(bulkloader.Loader):
	def __init__(self):
		bulkloader.Loader.__init__(self, 'Adventure', [('name', str)])

loaders = [AdventureLoader]