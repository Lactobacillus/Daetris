import os
import json
import pickle
import random
from flask import Flask, request, render_template, jsonify

count = 0
count_show = 2787
app = Flask(__name__)

with open('2017-1.pickle', 'rb') as f:

	lectures = pickle.load(f)

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():

	global count
	global count_show
	count += 1

	if request.method == 'GET':

		#string = request.args.get('string', '')
		#score, msg = scoring(string)
		string = ''
		score = ''
		msg = ''

	return render_template('index.html', cnt = str(count_show))

@app.route('/random', methods = ['GET'])
def randomLecture():

	global count
	global count_show
	global lectures
	count += 1
	count_show += 1

	point = 0
	sel_lectures = list()
	copy_lectures = list(lectures)
	random.shuffle(copy_lectures)

	for lec in copy_lectures:

		if point > 17:

			break

		else:

			temp = set()

			for sel in sel_lectures:

				temp = temp | set(sel['time'])

			if len(set(lec['time']) & temp) == 0:

				sel_lectures.append(lec)
				point = point + int(lec['hakjum'])

				for time in lec['time']:

					if int(time[1:]) > 8 or time[0] == '토':

						sel_lectures.pop()
						point = point - int(lec['hakjum'])

						break

			else:

				pass

	return render_template('random.html', selected = str(sel_lectures), hakjum = point)

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
	global count_show
	count += 1
	count_show += 1

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

	global count

	return '모든 page 에 대한 접근 : ' + str(count) + ' 회'

@app.route('/d3', methods = ['GET'])
def d3():

	return render_template('d3.html')

@app.route('/rawdata', methods = ['GET'])
def test(): 

	global lectures

	return str(json.dumps({'data':lectures}, ensure_ascii = False))

if __name__ == '__main__':

	#debug 모드 없애기#############################################
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port = port, debug = True)