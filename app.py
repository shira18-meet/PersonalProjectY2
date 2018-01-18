from flask import Flask,session, render_template
from flask_sqlalchemy import SQLAlchemy


import os

from sqlalchemy.orm import sessionmaker
from database import Base, Post #tables
##app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

from SQLAlchemy import create_engine, desc

engine = create_engine('sqlite:///project.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

db = SQLAlchemy(app)


@app.route('/')
@app.route('/feed')
def feed():
	posts=session.query(Post).order_by("id desc").all()
	return render_template('feed.html',posts=posts)

@app.route('/newyork')
def newyork():
	posts=session.query(Post).filter_by(city="New York").order_by('id desc').all()
	return render_template('feed.html',posts=posts)

@app.route('/texas')
def texas():
	posts=session.query(Post).filter_by(city="Texas").order_by('id desc').all()
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


