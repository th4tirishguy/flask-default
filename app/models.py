from . import db
class Player(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	player_name = db.Column(db.String(80), unique=True)
	gaming_system = db.Column(db.String(80))
	created_at = db.Column(db.DateTime())

	def __init__(self, pn, gs):
		self.player_name = pn
		self.gaming_system = gs
		self.DateTime = datetime.utcnow()
