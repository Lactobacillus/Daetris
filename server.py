import os
import pickle
from flask import Flask, request, render_template, redirect

count = 0
app = Flask(__name__)

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():

	count = count + 1

	if request.method == 'GET':

		#string = request.args.get('string', '')
		#score, msg = scoring(string)
		string = ''
		score = ''
		msg = ''

	return render_template('index.html', string = string, score = score, msg = msg)

@app.route('/draw', methods = ['GET'])
def draw():

	count = count + 1

	return render_template('draw.html')

@app.route('/map', methods = ['GET'])
def map():

	count = count + 1

	return render_template('map.html')

@app.route('/show', methods = ['GET', 'POST'])
def show():

	count = count + 1

	return render_template('show.html')

@app.route('/about', methods = ['GET'])
def about():

	count = count + 1

	return render_template('about.html')

@app.route('/traffic', methods = ['GET'])
def traffic():

	return count

if __name__ == '__main__':

	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port = port, debug = True)