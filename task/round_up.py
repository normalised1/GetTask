def round_up(num, val):
	if num % val != 0:
		return num + (val - (num % val))
	return num
