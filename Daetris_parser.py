import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import Daetris_functions as functions

def get_data_html():

	htmls = list()

	try:

		urls = functions.get_url_from_CSV('Daetris GET.csv')

		for url in urls:

			url = 'http://sugang.korea.ac.kr' + url
			html = urllib.request.urlopen(url)

			htmls.append(html)

	except Exception as e:

		functions.exception_info(e)

	finally:

		return htmls

def get_raw_info():

	lectures = list()

	try:

		htmls = get_data_html()

		for html in htmls:

			rows = BeautifulSoup(html).find_all('tbody').find_all('tr')

			for row in rows:

				lectures.append(row.find_all('td'))

	except Exception as e:

		functions.exception_info(e)

	finally:

		return lectures

def parse_info():

	lectures = list()

	try:

		raw_lectures = get_raw_info()

		for raw in raw_lectures:

			lecture = dict()

			lecture['code'] = raw[1].text.replace('\n', '')
			lecture['class'] = int(col[2].text)
			lecture['name'] = col[4].text.replace('\t', '').replace('\n', '').replace('\xa', '')
			lecture['professor'] = col[5].text
			lecture['point'] = col[6].text[2]
			lecture['time'] = time_to_schedule(col[7].text)

	except Exception as e:

		functions.exception_info(e)

	finally:

		datetime = functions.get_date()
		functions.serializer(datetime, lectures)

		return lectures

def time_to_schedule(text):

	# 1 ~ 66 (1교시 ~ 11교시 * 월요일 ~ 토요일)
	timeMap = [(0, '') for i in range(0, 67)]
	dayNum = {'월' : 1, '화' : 2, '수' : 3, '목' : 4, '금' : 5, '토' : 6}

	lines = text.split('\n')

	for line in lines:

		line = line.split(' ')
		day = line[0].split('(')[0]
		time = line[0].split('(')[1][:-1]

		if len(time) == 1:

			timeMap[dayNum[day] + 6 * (int(time) - 1)] = (1, str(line[1]) + ' ' + str(line[2]))

		elif len(time) == 3:

			time = time.split('-')

			for t in range(time[0], time[1] + 1):

				timeMap[dayNum[day] + 6 * (int(t) - 1)] = (1, str(line[1]) + ' ' + str(line[2]))

		else:

			pass

	return timeMap

if __name__ == '__main__':
    
	print(parse_info())
	
#계산은 element wise 덧셈 곱셈으로 