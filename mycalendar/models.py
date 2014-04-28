from google.appengine.ext import ndb

class Event(ndb.Model):
  title = ndb.StringProperty()