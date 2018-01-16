from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

##db = SQLAlchemy(app)
Base = declarative_base()

class Post(Base):
	__tablename__ = 'post'

	id = Column(Integer, primary_key=True)
	title=Column(String(80))
	city = Column(String(50))
	text = Column(String(300))


	def __init__(self,title,city,text):
		self.title=title
		self.city=city
		self.text=text

	def __repr__(self):
		return '<Title %r>' % self.title 