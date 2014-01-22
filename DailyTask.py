import sys
import datetime
sys.path.append('/home/normalised/webapps/get_task/htdocs')
sys.path.append('/home/normalised/webapps/get_task/htdocs/task')
from task.task import GetTask


def application(environ, start_response):
	date = datetime.datetime.now()
	day = date.day + 208 
	month = date.month
	year = date.year
	seed = day * 100 + month * 1000 + year
	output = '''<html><head></head>
<body>Daily task for <b>''' + datetime.date.today().strftime("%B %d, %Y") + '</b><h2>' + str(GetTask(seed)) + '</h2></body></html>'

	response_headers = [
		('Content-Length', str(len(output))),
		('Content-Type', 'text/html'),
	]

	start_response('200 OK', response_headers)

	return [output]
