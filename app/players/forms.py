from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class PlayerForm(Form):
	player_name = StringField('In Game Name')
	gaming_system = SelectField('Gaming System', choices=[('Xbox', 'Xbox'), 
		('Playstation', 'Playstation'), ('Steam', 'Steam')])
