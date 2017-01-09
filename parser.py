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
		html = response.read().decode('cp949')
		html = BeautifulSoup(unicodedata.normalize('NFKD', html))
		htmls.append(html)

		print(html)

	return htmls

if __name__ == '__main__':

	print(get_htmls('urlList.txt'))