       #flask shit



from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
import sys

##from flask import Flask,session, render_template
##from flask_sqlalchemy import SQLAlchemy


# SQLAlchemy shit
from sqlalchemy.orm import sessionmaker
from database import Base, Post #tables
from sqlalchemy import create_engine, desc


   #setup bro
engine = create_engine('sqlite:///project.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base.metadata.bind = engine

##db = SQLAlchemy(app)
##app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

@app.route('/')
@app.route('/feed')
def feed():
	posts=session.query(Post).order_by("id desc").all()
	return render_template('feed.html',posts=posts)


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/addpost',methods=['GET', 'POST'])
def addpost():
	if request.method == 'GET':
		return render_template('addpost.html')
	else:
		post_title = request.form.get('title')
		post_city = request.form.get('state')
		post_text = request.form.get('textish')
		thepost= Post(title=post_title,city=post_city,text=post_text)
		session.add(thepost)
		session.commit()
		return redirect(url_for('feed'))


@app.route('/new york')
def newyork():
	posts=session.query(Post).filter_by(city="New York").order_by('id desc').all()
	return render_template('feed.html',posts=posts)

@app.route('/texas')
def texas():
	posts=session.query(Post).filter_by(city="Texas").order_by('id desc').all()
	return render_template('feed.html',posts=posts)


@app.route('/california')
def california():
	posts=session.query(Post).filter_by(city="California").order_by('id desc').all()
	return render_template('feed.html',posts=posts)

@app.route('/washington')
def washington():
	posts=session.query(Post).filter_by(city="Washington").order_by('id desc').all()
	return render_template('feed.html',posts=posts)

@app.route('/florida')
def florida():
	posts=session.query(Post).filter_by(city="Florida").order_by('id desc').all()
	return render_template('feed.html',posts=posts)


@app.route('/hawaii')
def hawaii():
	posts=session.query(Post).filter_by(city="Hawaii").order_by('id desc').all()
	return render_template('feed.html',posts=posts)

@app.route('/other')
def other():
	posts=session.query(Post).filter_by(city="Other").order_by('id desc').all()
	return render_template('feed.html',posts=posts)

##@app.route('/posting', methods=['POST'])
##def posting():
	#post_title = request.form['title']
	#post_city = request.form['city']
	#post_text = request.form['textarea']
	#thepost= Post(title=post_title,city=post_city,text=post_text)
	#session.add(thepost)
	#session.commit()
	#return redirect(url_for('feed.html'))

Base.metadata.create_all()
