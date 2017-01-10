import pickle
import unicodedata
import urllib.request
from bs4 import BeautifulSoup

def save(fileName, target):

	f = open(fileName, 'wb')

	try:

		pickle.dump(target, f)

	except Exception as e:

		exception_info(e)

	finally:

		f.close()

def get_htmls(fileName):

	htmls = list()

	with open(fileName, 'r') as f:

		urls = f.readlines()

	for url in urls:

		response = urllib.request.urlopen(url)
		html = BeautifulSoup(response.read().decode('cp949'))
		htmls.append(html)

	return htmls

def get_time(text):

	time = list()

	for temp in text.split('\n'):

		temp = temp.split(' ')[0]

		if '-' in temp:

			for i in range(int(temp[2]), int(temp[4]) + 1):

				time.append(temp[0] + str(i))

		else:

			time.append(temp[0] + temp[2])

	return time

def get_room(text):

	room = list()

	for temp in text.split('\n'):

		room.append(temp.split(')')[1][1:])

	return list(set(room))

def get_lectures(htmls):

	lectures = list()

	for html in htmls:

		for row in html.find_all('tr'):

			lecture = dict()
			cols = row.find_all('td')

			if len(cols) == 17 and len(cols[7].text) > 0:

				try:

					lecture['haksu'] = cols[1].text.replace('\n', '')
					lecture['bunban'] = cols[2].text
					lecture['name'] = unicodedata.normalize('NFKC', cols[4].text.replace('\t', '').replace('\n', '').replace('\r', ''))[:-1]
					lecture['professor'] = cols[5].text
					lecture['hakjum'] = cols[6].text[2]
					lecture['time-room'] = cols[7].text
					lecture['time'] = get_time(cols[7].text)
					lecture['room'] = get_room(cols[7].text)

					print(lecture)

					lectures.append(lecture)
				
				except:

					pass

	return lectures

if __name__ == '__main__':

	# run in linux
	htmls = get_htmls('urlList.txt')
	lectures = get_lectures(htmls)
	save('2016-2.pickle', lectures)
	print(len(lectures))