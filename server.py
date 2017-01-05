import os
import pickle
from flask import Flask, request, render_template, redirect

count = [0]
app = Flask(__name__)

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():

	count[0] += 1

	if request.method == 'GET':

		#string = request.args.get('string', '')
		#score, msg = scoring(string)
		string = ''
		score = ''
		msg = ''

	return render_template('index.html', string = string, score = score, msg = msg)

@app.route('/draw', methods = ['GET'])
def draw():

	count[0] += 1

	return render_template('draw.html')

@app.route('/map', methods = ['GET'])
def map():

	count[0] += 1

	return render_template('map.html')

@app.route('/show', methods = ['GET', 'POST'])
def show():

	count[0] += 1

	return render_template('show.html')

@app.route('/about', methods = ['GET'])
def about():

	count[0] += 1

	return render_template('about.html')

@app.route('/traffic', methods = ['GET'])
def traffic():

	return str(count[0])

@app.route('/d3', methods = ['GET'])
def d3():

	return render_template('d3.html')

if __name__ == '__main__':

	count = [0]
	#debug 모드 없애기#############################################
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port = port, debug = True)