import os
import sys
import inspect
import datetime
import pickle

def get_datetime():

	return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

def exception_info(e):

	caller = inspect.stack()[1][3]

	print('There is Error')
	print('Caller : ' + caller + '(' + str(inspect.getargspec(caller)[0])[1:-1] + ')')
	print('Exception Type : ' + type(e).__name__)
	print('Timestamp : ' + str(datetime.datetime.now()))

def get_url_from_CSV(filename):

	url = list()
	f = open(filename, 'r')

	try:

		texts = f.readlines()

		for text in texts:

			url.append(eval(text)[6].replace('GET ', '').replace(' HTTP/1.1 ', ''))

	except Exception as e:

		exception_info(e)

	finally:

		f.close()

	return url

def serializer(filename, target):

	f = open(filename, 'wb')

	try:

		pickle.dump(target, f)

	except Exception as e:

		exception_info(e)

	finally:

		f.close()

def deserializer(filename):

	f = open(filename, 'rb')

	try:

		var = pickle.load(f)

	except Exception as e:

		var = None
		exception_info(e)

	finally:

		f.close()
		return var
