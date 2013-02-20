from google.appengine.ext import db

class Event(db.Model):
    title = db.StringProperty(required=True)
    description = db.TextProperty()
    time = db.DateTimeProperty()
    location = db.TextProperty()
    creator = db.StringProperty()
    
    
class Attendee(db.Model):
    email = db.StringProperty()
    event = db.ReferenceProperty(Event)
    
    
