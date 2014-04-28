import mycalendar
import mycalendar.models
import datetime



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
			'colours': mycalendar.models.COLOURS
		}

		self.render_template("new", template_values)

	def post(self):

		title = self.request.get("title")
		description = self.request.get("description")
		datestr = self.request.get("date")
		date = datetime.datetime.strptime(datestr, '%d-%m-%Y').date()
		colour = self.request.get('colour')
		
		event = mycalendar.models.Event(
			title = title,
			description = description,
			date = date,
			colour = colour
		)
		event.put()
		#what if its fails or user enters bad data?


		self.redirect("/agenda")
		