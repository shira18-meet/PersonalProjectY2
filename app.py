#flask shit



from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
import sys


# SQLAlchemy shit
from sqlalchemy.orm import sessionmaker
from database import Base,Rating, Post #tables
from sqlalchemy import create_engine, desc


#setup bro
engine = create_engine('sqlite:///project.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base.metadata.bind = engine


@app.route('/')
@app.route('/feed')
def feed():
	posts=session.query(Post).order_by("id desc").all()
	return render_template('feed.html',posts=posts, place="Recents feed")

@app.route('/rated')
def rated():
	posts=session.query(Post).order_by("av_rating desc").all()
	return render_template('feed.html',posts=posts, place="Best rated posts")




@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/addpost',methods=['GET', 'POST'])
def addpost():
	if request.method == 'GET':
		return render_template('addpost.html')
	else:
		post_title = request.form.get('title')
		post_continent = request.form.get('continent')
		post_country = request.form.get('country')
		post_city = request.form.get('city')
		post_text = request.form.get('textish')
		post_pic_url=request.form.get('pic_url')
		thepost= Post(title=post_title,continent=post_continent,country=post_country,city=post_city,text=post_text, img_url=post_pic_url)
		session.add(thepost)
		session.commit()
		return redirect(url_for('feed'))


@app.route('/Asia')
def Asia():
	posts=session.query(Post).filter_by(continent="Asia").order_by('id desc').all()
	return render_template('feed.html',posts=posts, place="Asia")

@app.route('/North_America')
def North_America():
	posts=session.query(Post).filter_by(continent="North_America").order_by('id desc').all()
	return render_template('feed.html',posts=posts, place="North America")


@app.route('/South_America')
def South_America():
	posts=session.query(Post).filter_by(continent="South_America").order_by('id desc').all()
	return render_template('feed.html',posts=posts, place="South America")

@app.route('/Europe')
def Europe():
	posts=session.query(Post).filter_by(continent="Europe").order_by('id desc').all()
	return render_template('feed.html',posts=posts, place="Europe")

@app.route('/Africa')
def Africa():
	posts=session.query(Post).filter_by(continent="Africa").order_by('id desc').all()
	return render_template('feed.html',posts=posts, place="Africa")


@app.route('/Australia')
def Australia():
	posts=session.query(Post).filter_by(continent="Australia").order_by('id desc').all()
	return render_template('feed.html',posts=posts, place="Australia")

@app.route('/Antartica')
def Antartica():
	posts=session.query(Post).filter_by(continent="Antartica").order_by('id desc').all()
	return render_template('feed.html',posts=posts, place="Antartica")


@app.route('/rate/<int:post_id>', methods=["POST", "GET"])
def rate(post_id):
	if request.method=="POST":
		this_post = session.query(Post).filter_by(id=post_id).first()
		this_post.amount+=1
		tz=0


		rating=int(request.form.get('rating'))
		this_rate=Rating(rates=rating, parent_id=post_id)
		session.add(this_rate)
		session.commit()
		this_post_rates=session.query(Rating).filter_by(parent_id=post_id).all()
		for x in this_post_rates:
			j=x.rates
			tz+=j
		tz=float(tz)
		this_post.amount=float(this_post.amount)
		amount=tz/this_post.amount
		this_post.av_rating=amount
		session.commit()
	return redirect(url_for('feed'))

Base.metadata.create_all()
app.debug = True