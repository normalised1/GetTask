import json
import random
from round_up import round_up

def getTagSymbol(tag):
	return unicode('$' + tag.upper())

def getNumericalValue(selected_task, tagName):
	range_min_key = 'min_' + tagName
	range_max_key = 'max_' + tagName

	c = None
	if getTagSymbol(tagName) in selected_task['description']:
		min_value = 1
		if range_min_key in selected_task:
			min_value = selected_task[range_min_key]

		max_value = min_value
		if range_max_key in selected_task:
			max_value = selected_task[range_max_key]

		c = random.randint(min_value, max_value)
		if c > 100:
			c = round_up(c, 10)
		elif c > 20:
			c = round_up(c, 5)
	return c

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
	count = getNumericalValue(selected_task, 'count')
	if count != None:
		description = unicode.replace(description, getTagSymbol('count'), unicode(count))

	duration = getNumericalValue(selected_task, 'duration')
	if duration != None:
		description = unicode.replace(description, getTagSymbol('duration'), unicode(duration) + u' minutes')

	if 'items' in selected_task:
		item_index = random.randint(0, len(selected_task['items']) - 1)
		item = selected_task['items'][item_index]
		description = unicode.replace(description, getTagSymbol('item'), unicode(item))

	return description

if __name__ == "__main__":
	import datetime
	date = datetime.datetime.now()
	day = date.day + 102 
	month = date.month
	year = date.year
	seed = day * 100 + month * 1000 + year
	print GetTask(seed)

