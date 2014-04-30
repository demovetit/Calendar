import mycalendar
import mycalendar.forms
import mycalendar.models
import datetime
from google.appengine.ext import ndb


class Index(mycalendar.BaseHandler):

	def get(self):

		self.redirect("/monthly")

class Agenda(mycalendar.BaseHandler):

	def get(self):

		template_values = {
			"title": "Events",
			"events":  mycalendar.models.Event.query(mycalendar.models.Event.date >= datetime.date.today()).order(mycalendar.models.Event.date),
		}

		self.render_template("agenda", template_values)

	def post(self):

		self.redirect("/event/new")

class EventDelete(mycalendar.BaseHandler):
	
	def post(self):
		# import logging
		# logging.error(self.request.get("event_id"))
		
		entityid = self.request.get("event_id")


		ndb.Key(mycalendar.models.Event , int(entityid)).delete()

		self.redirect('/agenda')

class Monthly(mycalendar.BaseHandler):
	
	def get(self):

		template_values = {
			"title": "Events",
			"events":  mycalendar.models.Event.query(mycalendar.models.Event.date >= datetime.date.today()).order(mycalendar.models.Event.date),
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
			'colours': mycalendar.models.COLOURS
		}

		self.render_template("new", template_values)
	#Gets data from New.html
	def post(self):

		form = mycalendar.forms.NewEvent(self.request.POST)

		if form.validate():

			#Data Dictionary
			event = mycalendar.models.Event(
				title = form.title.data,
				description = form.description.data,
				date = form.date.data,
				colour = form.colour.data
			)
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




