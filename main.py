from flask import Flask, render_template
import model
from model import get_headlines
from plotly.offline import iplot
import random
from time import sleep

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/feed')
def feed():
  return render_template('feed.html', headlines = get_headlines())

@app.route('/trends')
def trends():
  return render_template('trends.html', num_fake = model.get_data("FAKE"), num_real = model.get_data("REAL"), num_clickbait = )
  

app.run(host='0.0.0.0', port=8080, debug=True)
