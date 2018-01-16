from flask import Flask
app = Flask(__name__)
from flask import render_template


@app.route('/')
@app.route('/feed')
def feed():
	return render_template('feed.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/addpost')
def addpost():
	return render_template('addpost.html')

