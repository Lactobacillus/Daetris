import os
import sys
from flask import Flask
from flask import *
import Daetris_functions as functions

app = Flask(__name__)
app.jinja_env.autoescape = False
using = None
lectures = None

@app.route('/')
def index():

	#GET_query = request.query_string
	#schedule = make_schedule(GET_query)
	#app.url_for('static', filename = 'index.html')

	return render_template('index.html', table = draw_table(None))

def server_main():

	app.run()

def make_schedule(query):

	if lectures == None or using != functions.get_date():

		using = functions.get_date()
		lectures = functions.deserializer(using)



#afdafdadfsdfsadfsadfsafdsafdsdfsafdsafdsadafsdafsss



def draw_table(schedule = None):

	table = '	<div id="table">\n'

	table += '    <div class="row">\n'
	table += '        <div><span class="leftspan"></span></div>\n'
	table += '        <div><span class="cellspan">월</span></div>\n'
	table += '        <div><span class="cellspan">화</span></div>\n'
	table += '        <div><span class="cellspan">수</span></div>\n'
	table += '        <div><span class="cellspan">목</span></div>\n'
	table += '        <div><span class="cellspan">금</span></div>\n'
	table += '        <div><span class="cellspan">토</span></div>\n'
	table += '    </div>\n'

	for idx in range(1, 67):

		if idx % 6 == 1:

			table += '    <div class="row" style="padding-bottom:2px;">\n'
			table += '        <div class="left"><span class="leftspan">{0}교시</span></div>\n'.format(int(idx / 6))

		if (6 < idx <= 18) or (30 < idx <= 42):

			table += '        <input onclick="clickButton({0})" class="bigcell" type="button" name="{1}" value="0">'.format(idx, idx)

		else:

			table += '        <input onclick="clickButton({0})" class="smallcell" type="button" name="{1}" value="0">'.format(idx, idx)

		if schedule != None:

			table += '{0}<br>{1}'.format(schedule[idx]['code'], schedule[idx]['name'])

		table += '</button>\n'

		if idx % 6 == 0:

			table += '    </div>\n'

	table = table + '</div>\n'

	return table

if __name__ == '__main__':
    
    server_main()