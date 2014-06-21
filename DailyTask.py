import sys
import datetime
sys.path.append('/home/normalised/webapps/get_task/htdocs')
sys.path.append('/home/normalised/webapps/get_task/htdocs/task')
from task.task import GetTask


def application(environ, start_response):
	previous = False
	tweak_value = 522
	fast_forward = 0
	if str(environ['QUERY_STRING'])=='previous':
		date = datetime.datetime.now() - datetime.timedelta(days=1)
		previous = True
	else:
		date = datetime.datetime.now()
		try:
			fast_forward = int(environ['QUERY_STRING'])
		except:
			pass

	day = date.day + fast_forward
	month = date.month
	year = date.year
	seed = (day + tweak_value) * 100 + month * 1000 + year
	task = str(GetTask(seed))

	# Hack to maintain the current day's task.
	# TODO: Can be removed
	if day == 22 and month == 6 and year == 2014:
		task = 'Edge 2 times with face in a toilet'

	output = '''<html><head><link rel="stylesheet" type="text/css" href="style.css"></head>
<body><br><p>Daily task for <b>''' + date.strftime("%B %d, %Y") + '</b><h2>{0}</h2></p>'''.format(task)
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
