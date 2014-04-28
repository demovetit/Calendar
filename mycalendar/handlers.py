import mycalendar
import mycalendar.models

class Index(mycalendar.BaseHandler):

	def get(self):

		self.redirect("/agenda")

class Agenda(mycalendar.BaseHandler):

	def get(self):

		template_values = {
			"title": "Events",
			"events":  mycalendar.models.Event.query()
		}

		self.render_template("agenda", template_values)

	def post(self):

		self.redirect("/new")

class New(mycalendar.BaseHandler):

	def get(self):

		template_values = {
		}

		self.render_template("new", template_values)

	def post(self):

		title = self.request.get("title")
		description = self.request.get("description")
		date = self.request.get("date")
		import logging
		logging.error(type(date))
		"""
		event = mycalendar.models.Event(
			title = title,
			description = description,
			date = date
		)
		event.put()
		#what if its fails or user enters bad data?


		self.redirect("/agenda")
		"""