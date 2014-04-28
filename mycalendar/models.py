from google.appengine.ext import ndb

class Event(ndb.Model):
  title = ndb.StringProperty()
  description = ndb.StringProperty()
  date = ndb.DateProperty()
