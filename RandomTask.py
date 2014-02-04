import sys
import datetime
sys.path.append('/home/normalised/webapps/get_task/htdocs')
sys.path.append('/home/normalised/webapps/get_task/htdocs/task')
from task.task import GetTask


def application(environ, start_response):
	try:
		seed = int(environ['QUERY_STRING'])
	except:
		seed = datetime.datetime.now().microsecond

	output = '<html><head><link rel="stylesheet" type="text/css" href="style.css"></head><body><br><p><b>Random</b> task:<h2>' + str(GetTask(seed))+ '</h2></p><a href="random_task">another</a></body></html>'

	response_headers = [
		('Content-Length', str(len(output))),
		('Content-Type', 'text/html'),
	]

	start_response('200 OK', response_headers)

	return [output]
