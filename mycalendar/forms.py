from wtforms import Form, StringField
from wtforms import validators

class NewEvent(Form):

	title = StringField(
		default="",
		label="Title",
		description="Enter your title here!!!",
		validators=[
			validators.DataRequired()
		]
	)

	description = StringField(
		label="Description",
		validators=[
			validators.DataRequired()
		]
	)