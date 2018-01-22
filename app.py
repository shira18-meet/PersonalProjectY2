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

@app.route('/rated')
def rated():
	posts=session.query(Post).order_by("av_rating desc").all()
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


@app.route('/rate/post_id')
def rate(post_id):
	this_post = session.query(Post).filter_by(id=post_id).first()
	this_post.amount+=1
	tz=0
	
	this_post_rates=session.query(Rating).filter_by(id=this_post).all()
	rating=request.form.get('rating')
	this_rate=Rating(rates=rating, parent_id=this_post.id)
	for x in this_post_rates:
		tz+=x.rates
	avrage=tz/this_post.amount
	this_post.av_rating=avrage
	session.add(this_rate)
	session.commit()
	return redirect(url_for('feed.html'))

Base.metadata.create_all()
