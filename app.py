from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from database import Base, Post #tables
app = Flask(__name__)
from flask import render_template
##app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

@app.route('/')
@app.route('/feed')
def feed():
	posts=session.query(Post).order_by("id desc").all()
	return render_template('feed.html',posts=posts)


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/addpost')
def addpost():
	return render_template('addpost.html')


@app.route('/posting', methods=['POST'])
def posting():
	post_title = request.form['title']
	post_city = request.form['city']
	post_text = request.form['textarea']
	thepost= Post(title=post_title,city=post_city,text=post_text)
	session.add(thepost)
	session.commit(thepost)
	return render_template('feed.html')


