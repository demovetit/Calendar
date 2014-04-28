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

class New(mycalendar.BaseHandler):

	def get(self):

		template_values = {
		}

		self.render_template("new", template_values)

	def post(self):

		title = self.request.get("title")

		event = mycalendar.models.Event(
			title = title
		)
		event.put()
		#what if its fails or user enters bad data?

		self.redirect("/agenda")