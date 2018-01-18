from flask import Flask,session, render_template
import os
app = Flask(__name__)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/')
@app.route('/feed')
def feed():
	posts=session.query(Post).order_by("id desc").all()
	return render_template('feed.html',posts=posts)