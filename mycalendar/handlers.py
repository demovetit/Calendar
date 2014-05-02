import mycalendar
import mycalendar.forms
import mycalendar.models
from datetime import date
from datetime import timedelta
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import mail
import datetime




class Index(mycalendar.BaseHandler):

	def get(self):

		start_date = date.today()

		end_date = start_date + timedelta(days=7)

		events = mycalendar.models.Event.query().filter(
			mycalendar.models.Event.date >= start_date,
			mycalendar.models.Event.date <= end_date,
		)
		if events.count() > 0 :

			userid = users.get_current_user()
			userEmailId = userid.email()

			mail.send_mail(sender="Kalsync.com <demovetit@gmail.com>",
			              to=userEmailId,
			              subject="Upcoming Event",
			              body="""
			Dear User:
			An upcoming event is fast approaching, please check your calendar to see the event.

			""")

		self.redirect("/monthly")

class Agenda(mycalendar.BaseHandler):

	def get(self):

		template_values = {
			"title": "Events",
			"events":  mycalendar.models.Event.query(mycalendar.models.Event.date >= date.today()).filter(mycalendar.models.Event.owner == users.get_current_user()).order(mycalendar.models.Event.date),
		}

		self.render_template("agenda", template_values)

	def post(self):

		self.redirect("/event/new")

class EventDelete(mycalendar.BaseHandler):
	
	def post(self):
		
		entityid = self.request.get("event_id")


		ndb.Key(mycalendar.models.Event , int(entityid)).delete()

		
		self.redirect('/agenda')

class Monthly(mycalendar.BaseHandler):
	
	def get(self):

		today = date.today()

		start_date = date(today.year, today.month, 1)

		#go back to previous monday
		if start_date.weekday() != 0:
			start_date = start_date + timedelta(days=-start_date.weekday())

		end_date = start_date + timedelta(days=34)

		events = mycalendar.models.Event.query().filter(
			mycalendar.models.Event.date >= start_date,
			mycalendar.models.Event.date <= end_date,
			mycalendar.models.Event.owner == users.get_current_user(),
		)

		weeks = list()
		day_of_month = start_date
		for i in range(5):#Weeks Loop
			
			weeks.append(list())
			
			for j in range(7): #Days Loop
				weeks[i].append(list())

				for event in events:
					if event.date == day_of_month:
						weeks[i][j].append(event)

				day_of_month = day_of_month + timedelta(days=1)

		template_values = {
			"title": "Events",
			"table_title": today.strftime('%B %Y'),
			"weeks": weeks
		}

		self.render_template("monthly", template_values)

	def post(self):

		self.redirect("/event/new")


class EventEdit(mycalendar.BaseHandler):

	def get(self):

		event_id = int(self.request.get("event_id"))

		event_key = ndb.Key("Event", event_id)
		event = event_key.get()

		if event is None:
			self.response.status = 404
			return
		form = mycalendar.forms.NewEvent()
		form.title.data = event.title
		form.description.data = event.description
		form.date.data = event.date
		form.colour.data = event.colour

		template_values = {
			"updated": False,
			"form": form,
			"colours": mycalendar.models.COLOURS
		}

		self.render_template("edit", template_values)

	def post(self):

		event_id = int(self.request.get("event_id"))

		event_key = ndb.Key("Event", event_id)
		event = event_key.get()
		if event is None:
			self.response.status = 404
			return

		form = mycalendar.forms.NewEvent(self.request.POST)

		if form.validate():
			
			event.title = form.title.data
			event.description = form.description.data
			event.date = form.date.data
			event.colour = form.colour.data
			event.put()
			template_values = {
				'updated': True,
				'form': form,
				'colours': mycalendar.models.COLOURS
			}
			userid = users.get_current_user()
			userEmailId = userid.email()

			mail.send_mail(sender="Kalsync.com <demovetit@gmail.com>",
			              to=userEmailId,
			              subject="Edited Event",
			              body="""
			Dear User:
			
			Congratulations on editing an existing event to your calendar.

			""")


			self.render_template("edit", template_values)

		else:

			#if date validation fails then reset to an empty string
			if form.date.data is None:
				form.date.data = ""
		
			template_values = {
				'updated': False,
				'form': form,
				'colours': mycalendar.models.COLOURS
			}

			self.render_template("edit", template_values)




class EventNew(mycalendar.BaseHandler):

	def get(self):

		template_values = {
			'form': mycalendar.forms.NewEvent(),
			'colours': mycalendar.models.COLOURS,
		}

		self.render_template("new", template_values)
	#Gets data from New.html
	def post(self):

		form = mycalendar.forms.NewEvent(self.request.POST)
		userid = users.get_current_user()
		userEmailId = userid.email()

		if form.validate():

			#Data Dictionary
			event = mycalendar.models.Event(
				title = form.title.data,
				description = form.description.data,
				date = form.date.data,
				colour = form.colour.data,
				owner = users.get_current_user()
			)
			

			mail.send_mail(sender="Kalsync.com <demovetit@gmail.com>",
			              to=userEmailId,
			              subject="New Event",
			              body="""
			Dear User:
			
			Congratulations on adding a new event to your calendar.

			""")

			event.put()

			self.redirect("/agenda")
		else:

			#if date validation fails then reset to an empty string
			if form.date.data is None:
				form.date.data = ""

			template_values = {
				'form': form,
				'colours': mycalendar.models.COLOURS
			}

			self.render_template("new", template_values)




