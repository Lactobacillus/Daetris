from flask.ext.sqlalchemy import SQLAlchemy
from app import app
db = SQLAlchemy(app)

class Visitor(db.Model):

	__tablename__ = 'visitor'
	id = db.Column(db.Integer, primary_key = True)
	count = db.Column(db.Integer)

	def __init__(self, visitor):

		self.count = count

	def __repr__(self):

		return '<visitor %r>' % self.visitor