from flask import Flask, render_template, request
import model
from model import get_headlines
from plotly.offline import iplot

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    url = request.form['url']
    predict = model.predict(url)
    value = predict[1]
    clickbait = predict[2]
    return render_template('index.html', value = value, clickbait = clickbait)
  else:
    return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/feed')
def feed():
  str1 = ""
  headlines = get_headlines()
  url = headlines[0]
  url = url[0]
  for letter in url:
    str1 += letter
  return render_template('feed.html', headlines = headlines, predict = model.predict(str1))

@app.route('/trends')
def trends():
  return render_template('trends.html', num_fake = model.get_data("FAKE"), num_real = model.get_data("REAL"), num_clickbait = model.get_data("CLICKBAIT"), num_notclickbait = model.get_data("NOT CLICKBAIT"))
 

app.run(host='0.0.0.0', port=8080, debug=True)
