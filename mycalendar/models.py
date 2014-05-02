from google.appengine.ext import ndb
from google.appengine.api import mail
from google.appengine.api import users
import datetime

USERID:users.get_current_user(),
COLOURS = ['none', 'blue', 'green', 'red', 'dark-blue']

#Puts data from the server
class Event(ndb.Model):
  title = ndb.StringProperty(required = True)
  description = ndb.StringProperty()
  date = ndb.DateProperty(required = True)
  colour = ndb.StringProperty(choices = COLOURS)
  searchid = ndb.StringProperty(required = True)

  #Converts the Date Format
  @property
  def date_formatted(self):
	return datetime.datetime.strftime(self.date, '%d %B %Y')

  @property
  def only_date(self):
  	return datetime.datetime.strftime(self.date, '%d')