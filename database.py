from flask import Flask,session
##from Flask_SQLAlchemy import SQLAlchemy

from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
#import os
from sqlalchemy.orm import relationship

#from SQLAlchemy import create_engine, desc
#from sqlalchemy.orm import sessionmaker
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
#engine = create_engine('sqlite:///project.db')
#DBSession = sessionmaker(bind=engine)
#session = DBSession()

#app = Flask(__name__)
#db = SQLAlchemy(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
Base = declarative_base()

class Post(Base):
	__tablename__ = 'post'

	id = Column(Integer, primary_key=True)
	title=Column(String(80))
	city = Column(String(50))
	text = Column(String(300))
	amount = Column(Integer, default=0)
	av_rating=Column(Integer)
	rate = relationship("Rating")


	def __init__(self,title,city,text):
		self.title=title
		self.city=city
		self.text=text

	def __repr__(self):
		return '<Title %r>' % self.title 

class Rating(Base):
	__tablename__='Rating'

	id  = Column(Integer, primary_key=True)
	rates=Column(Integer)
	parent_id = Column(Integer, ForeignKey('post.id'))

	def __init__(self, rate):
		self.rating=rate;