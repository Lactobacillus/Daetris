import os
import pickle
from flask import Flask, request, render_template, redirect

count = 0
app = Flask(__name__)

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():

	global count
	count += 1

	if request.method == 'GET':

		#string = request.args.get('string', '')
		#score, msg = scoring(string)
		string = ''
		score = ''
		msg = ''

	return render_template('index.html', string = string, score = score, msg = msg)

@app.route('/draw', methods = ['GET'])
def draw():

	global count
	count += 1

	return render_template('draw.html')

@app.route('/map', methods = ['GET'])
def map():

	global count
	count += 1

	return render_template('map.html')

@app.route('/show', methods = ['GET', 'POST'])
def show():

	global count
	count += 1

	if request.method == 'POST':
		
		if asdf:

			# draw 에서 왔을 때
			return render_template('show.html')
			return str(request.form['c11'])

		elif sadf:

			# map 에서 왔을 때
			pass

		else:

			return render_template('draw.html')

	else:

		return render_template('draw.html')

@app.route('/about', methods = ['GET'])
def about():

	global count
	count += 1

	return render_template('about.html')

@app.route('/traffic', methods = ['GET'])
def traffic():

	return '모든 page 에 대한 접근 : ' + str(count[0]) + ' 회'

@app.route('/d3', methods = ['GET'])
def d3():

	return render_template('d3.html')

if __name__ == '__main__':

	#debug 모드 없애기#############################################
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port = port, debug = True)