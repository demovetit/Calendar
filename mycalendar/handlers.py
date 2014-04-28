import mycalendar

class Event(mycalendar.BaseHandler):

	def get(self):
		self.response.out.write("Test")