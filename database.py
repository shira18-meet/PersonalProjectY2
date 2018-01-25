from flask import Flask,session
##from Flask_SQLAlchemy import SQLAlchemy

from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey, Float
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
	__tablename__ = 'Post'

	id = Column(Integer, primary_key=True)
	title=Column(String(80))
	city = Column(String(50))
	text = Column(String(300))
	img_url=Column(String(100),default=None)
	amount = Column(Float, default=0)
	av_rating=Column(Float)
	rate = relationship("Rating")


	def __init__(self,title,city,text,img_url):
		self.title=title
		self.city=city
		self.text=text
		self.img_url=img_url

	def __repr__(self):
		return '<Title %r>' % self.title 

class Rating(Base):
	__tablename__='Rating'

	id  = Column(Integer, primary_key=True)
	rates=Column(Integer)
	parent_id = Column(Integer, ForeignKey('Post.id'))

	def __init__(self, rates ,parent_id):
		self.rates=rates
		self.parent_id=parent_id



