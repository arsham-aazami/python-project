def mile_marathon(portions_list):
	marathon_length = 0
	for portion in portions_list:
		marathon_length += portion
	if marathon_length == 25:
		return True
	else:
		return False


mile_marathon([1, 9, 5, 8, 2])
