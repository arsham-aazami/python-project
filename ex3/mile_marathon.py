def mile_marathon(portions_list):
	"""
	:param portions_list: a list including marathon's length
	:return: boolean
	"""
	marathon_length = 0
	for portion in portions_list:
		if portion < 0:
			portion *= -1
		marathon_length += portion
	if marathon_length == 25:
		return True
	else:
		return False


print(mile_marathon([-6, 15, 4]))
