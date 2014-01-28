import sys
import datetime
sys.path.append('/home/normalised/webapps/get_task/htdocs')
sys.path.append('/home/normalised/webapps/get_task/htdocs/task')
from task.task import GetTask


def application(environ, start_response):
	previous = False
	if str(environ['QUERY_STRING'])=='previous':
		date = datetime.datetime.now() - datetime.timedelta(days=1)
		previous = True
	else:
		date = datetime.datetime.now()

	day = date.day + 213 
	month = date.month
	year = date.year
	seed = day * 100 + month * 1000 + year

	output = '''<html><head><link rel="stylesheet" type="text/css" href="style.css"></head>
<body><br><p>Daily task for <b>''' + date.strftime("%B %d, %Y") + '</b><h2>' + str(GetTask(seed)) + '</h2></p>'

	if previous != True:
		output += '<a href="daily_task?previous">yesterday</a>'
	else:
		output += '<a href="daily_task">today</a>'

	output += '</body></html>'

	response_headers = [
		('Content-Length', str(len(output))),
		('Content-Type', 'text/html'),
	]

	start_response('200 OK', response_headers)

	return [output]
