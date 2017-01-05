import os
import pickle
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():

	if request.method == 'GET':

		#string = request.args.get('string', '')
		#score, msg = scoring(string)
		string = ''
		score = ''
		msg = ''

	return render_template('index.html', string = string, score = score, msg = msg)

@app.route('/draw', methods = ['GET'])
def draw():

	return render_template('draw.html')

@app.route('/map', methods = ['GET'])
def map():

	return render_template('map.html')

@app.route('/show', methods = ['GET', 'POST'])
def show():

	return render_template('show.html')

if __name__ == '__main__':

	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port = port, debug = True)