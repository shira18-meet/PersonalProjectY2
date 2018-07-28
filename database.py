from flask import Flask,session
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Post(Base):
	__tablename__ = 'Post'

	id = Column(Integer, primary_key=True)
	title=Column(String(80))
	continent= Column(String(50))
	country = Column(String(50))
	city = Column(String(50))
	text = Column(String(300))
	img_url=Column(String(100),default=None)
	amount = Column(Float, default=0)
	av_rating=Column(Float)
	rate = relationship("Rating")


	def __init__(self,title,continent,country,city,text,img_url):
		self.title=title
		self.continent=continent
		self.country=country
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



