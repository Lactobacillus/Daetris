import os
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

def scoring(string):

	score = 0
	u_string = string.upper()

	for char in u_string:

		if 64 < ord(char) and ord(char) <= 90:

			score = score + ord(char) - 64

	if score == 100:

		msg = '꺄오~ 축하합니다! 100점짜리 인생이네요!'

	elif 0 < score < 60:

		msg = '시무룩한 점수네요.'

	elif 60 <= score < 90:

		msg = '그럴싸한 점수네요.'

	elif 90 <= score < 100:

		msg = '앗! 뭔가가 더 필요합니다!'

	elif 100 < score <= 150:

		msg = '와우! 가치가 폭발했네요!'

	elif 200 < score:

		msg = '좀 짧게 써야할 것 같아요!'

	else:

		msg = ''

	return str(score), msg

@app.route('/', methods = ['GET'])
def index():

	if request.method == 'GET':

		string = request.args.get('string', '')
		score, msg = scoring(string)
	
		if 'HEROESOFTHESTORM' in string.upper().replace(' ', ''):

			return redirect('http://kr.battle.net/heroes/ko/', code = 302)

	return render_template('index.html', string = string, score = score, msg = msg)

if __name__ == '__main__':
    
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port = port)