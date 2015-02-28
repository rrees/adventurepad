from google.appengine.ext import db

class Adventure(db.Model):
	name = db.StringProperty(required=True)

class CharacterAttributes(db.Expando):
	items = db.StringListProperty()

class Character(db.Model):
	ownert = db.UserProperty(required=True)
	name = db.StringProperty(required=True)
	attributes = db.ReferenceProperty(CharacterAttributes)
	

class Session(db.Model):
	user = db.UserProperty(required=True)
	current_entry = db.IntegerProperty()
	character = db.ReferenceProperty(Character)
	