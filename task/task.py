import json
import random

def GetTask(seed):
	import os
	# Change directory so data.json can be foun d
	os.chdir('/home/normalised/webapps/get_task/htdocs')

	f = file('data.json')
	objects = json.load(f)
	random.seed(seed)
	value = random.randint(0, len(objects) - 1)
	selected_task = None
	for key in objects:
		value = value - 1
		selected_task = objects[key]
		if value < 0:
			break

	description = selected_task['description']
	if 'min_count' in selected_task:
		min_count = selected_task['min_count']
		max_count = min_count
		if 'max_count' in selected_task:
			max_count = selected_task['max_count']

		c = random.randint(min_count, max_count)
		description = unicode.replace(selected_task['description'], u'$COUNT', unicode(c))

	if 'min_duration' in selected_task:
		min_duration = selected_task['min_duration']
		max_duration = min_duration
		if 'max_duration' in selected_task:
			max_duration = selected_task['max_duration']

		c = random.randint(min_duration, max_duration)
		description = unicode.replace(description, u'$DURATION', unicode(c) + u' minutes')

	if 'items' in selected_task:
		item_index = random.randint(0, len(selected_task['items']) - 1)
		item = selected_task['items'][item_index]
		description = unicode.replace(description, u'$ITEM', unicode(item))

	return description

if __name__ == "__main__":
	import datetime
	date = datetime.datetime.now()
	day = date.day + 102 
	month = date.month
	year = date.year
	seed = day * 100 + month * 1000 + year
	print GetTask(seed)

