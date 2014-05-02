from wtforms import Form, StringField
from wtforms import DateField
from wtforms import validators
from datetime import date
import mycalendar.models

class NewEvent(Form):

	title = StringField(
		default="",
		label="Title",
		description="Title(Required)",
		validators=[
			validators.InputRequired()
		]
	)

	description = StringField(
		label="Description",
		description="",
		default="",
		
	)

	date = DateField(
		label="Date",
		description="yyyy-mm-dd",
		default=date.today(),
		validators=[
			validators.InputRequired()
		]
	)

	colour = StringField(
		default=mycalendar.models.COLOURS[0],
		label="Colour",
		validators=[
			validators.InputRequired(),
			validators.AnyOf(mycalendar.models.COLOURS)
		]
	)

