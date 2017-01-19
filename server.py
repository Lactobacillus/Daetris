import os
import json
import pickle
import random
from flask import Flask, request, render_template

visitor = 0
app = Flask(__name__)

with open('2017-1.pickle', 'rb') as f:

	lectures = pickle.load(f)

with open('visitor.pickle', 'rb') as f:

	visitor = pickle.load(f)

def randomLecture(lower, upper, rooms = None):

	global lectures

	point = 0
	selected = list()

	if rooms == None:

		lec_pool = list(lectures)

	else:

		lec_pool = list()

		for lec in lectures:

			for room in lec['room']:

				if any(r in room for r in rooms):

					lec_pool.append(lec)

	random.shuffle(lec_pool)

	for lec in lec_pool:

		if point > lower:

			break

		else:

			temp = set()

			for sel in selected:

				temp = temp | set(sel['time'])

			if len(set(lec['time']) & temp) == 0 and upper >= point + int(lec['hakjum']):

				selected.append(lec)
				point = point + int(lec['hakjum'])

				for time in lec['time']:

					if int(time[1:]) > 8 or time[0] == '토':

						selected.pop()
						point = point - int(lec['hakjum'])

						break

			else:

				pass

	return selected, point

def makeDrawLecture(req, trial):

	lower = 0
	candidate = list()
	cand_hakjum = list()
	similarity = list()
	day = {'월' : 1, '화' : 2, '수' : 3, '목' : 4, '금' : 5}

	for key in req:

		if int(key[1]) in [1, 2, 5, 6]:

			lower += float(req[key]) * 1.5

		else:

			lower += float(req[key]) * 1

	for idx in range(0, trial):

		lecture, hakjum = randomLecture(int(lower) - 1, int(lower) + 1)
		candidate.append(lecture)
		cand_hakjum.append(hakjum)

	for cand in candidate:

		times = set()

		for lec in cand:

			point = 0

			for t in lec['time']:

				times = times | {'c' + t[1] + str(day[t[0]])}

		for key in req:

			if int(req[key]) == 1:

				if key in times:

					point += 1

				else:

					point -= 2

			else:

				if key not in times:

					point += 1

				else:

					point -= 2

		similarity.append(point)

	for idx in range(0, trial):

		if similarity[idx] == max(similarity):

			selected = candidate[idx]
			selected_hakjum = cand_hakjum[idx]

			break

	return selected, selected_hakjum

def makeMapLecture(req):

	rooms = list()

	for key in req:

		if int(req[key]) == 1:

			rooms.append(key)

	lecture, hakjum = randomLecture(17, 22, rooms)

	return lecture, hakjum

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():

	global visitor

	return render_template('index.html', cnt = str(visitor))

@app.route('/random', methods = ['GET'])
def randomShow():

	global visitor
	visitor += 1

	with open('visitor.pickle', 'wb') as f:

		pickle.dump(visitor, f)

	result, point = randomLecture(17, 22)

	return render_template('random.html', selected = str(result), hakjum = point)

@app.route('/draw', methods = ['GET'])
def draw():

	return render_template('draw.html')

@app.route('/map', methods = ['GET'])
def map():

	return render_template('map.html')

@app.route('/show', methods = ['GET', 'POST'])
def show():

	global visitor
	visitor += 1

	with open('visitor.pickle', 'wb') as f:

		pickle.dump(visitor, f)

	if request.method == 'POST':
		
		if len(request.form) == 40:

			# draw 에서 왔을 때
			result, point = makeDrawLecture(request.form, 500)

			return render_template('show.html', selected = str(result), hakjum = point)

		elif len(request.form) == 28:

			# map 에서 왔을 때
			result, point = makeMapLecture(request.form)

			return render_template('show.html', selected = str(result), hakjum = point)

		else:

			return render_template('draw.html')

	else:

		return render_template('draw.html')

@app.route('/about', methods = ['GET'])
def about():

	return render_template('about.html')

@app.route('/traffic', methods = ['GET'])
def traffic():

	global visitor

	return '모든 page 에 대한 접근 : ' + str(visitor) + ' 회'

@app.route('/d3', methods = ['GET'])
def d3():

	return render_template('d3.html')

if __name__ == '__main__':

	#debug 모드 없애기#############################################
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port = port, debug = True)