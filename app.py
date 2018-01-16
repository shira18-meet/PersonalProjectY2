from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask
app = Flask(__name__)
from flask import render_template
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

@app.route('/')
@app.route('/feed')
def feed():
	return render_template('feed.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/addpost', methods=['POST'])
def addpost():
	title = request.form['title']
	city = request.form['city']
	text = request.form['text']

	return render_template('addpost.html')


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title=db.Column(db.String(80))
	city = db.Column(db.String(50))
	text = db.Column(db.String(300))


	def __init__(self,title,city,text):
		self.title=title
		self.city=city
		self.text=text

	def __repr__(self):
		return '<Title %r>' % self.title 
