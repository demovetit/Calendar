from google.appengine.ext import ndb
import datetime

COLOURS = ['blue', 'green', 'red']

#Puts data from the server
class Event(ndb.Model):
  title = ndb.StringProperty(required = True)
  description = ndb.StringProperty()
  date = ndb.DateProperty(required = True)
  colour = ndb.StringProperty(choices = COLOURS)

  #Converts the Date Format
  @property
  def date_formatted(self):
	return datetime.datetime.strftime(self.date, '%d %B %Y')
  	
