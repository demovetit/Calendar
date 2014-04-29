import mycalendar
import mycalendar.forms
import mycalendar.models
import datetime



class Index(mycalendar.BaseHandler):

	def get(self):

		self.redirect("/agenda")

class Agenda(mycalendar.BaseHandler):

	def get(self):

		template_values = {
			"title": "Events",
			"events":  mycalendar.models.Event.query().order(mycalendar.models.Event.date)
		}

		self.render_template("agenda", template_values)

	def post(self):

		self.redirect("/new")

class New(mycalendar.BaseHandler):

	def get(self):

		template_values = {
			'form': mycalendar.forms.NewEvent(),
			'colours': mycalendar.models.COLOURS
		}

		self.render_template("new", template_values)
	#Gets data from New.html
	def post(self):

		"""
		title = self.request.get("title")
		description = self.request.get("description")
		datestr = self.request.get("date")
		date = datetime.datetime.strptime(datestr, '%d-%m-%Y').date()
		colour = self.request.get('colour')
		"""
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