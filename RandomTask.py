import sys
import datetime
sys.path.append('/home/normalised/webapps/get_task/htdocs')
from task.task import GetTask


def application(environ, start_response):
	date = datetime.datetime.now()
	output = str(GetTask(date.microsecond))

	response_headers = [
		('Content-Length', str(len(output))),
		('Content-Type', 'text/plain'),
	]

	start_response('200 OK', response_headers)

	return [output]
