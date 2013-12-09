import sys
import datetime
sys.path.append('/home/normalised/webapps/get_task/htdocs')
sys.path.append('/home/normalised/webapps/get_task/htdocs/task')
from task.task import GetTask


def application(environ, start_response):
	date = datetime.datetime.now()
	day = date.day + 118 
	month = date.month
	year = date.year
	seed = day * 100 + month * 1000 + year
	output = str(GetTask(seed))

	response_headers = [
		('Content-Length', str(len(output))),
		('Content-Type', 'text/plain'),
	]

	start_response('200 OK', response_headers)

	return [output]
