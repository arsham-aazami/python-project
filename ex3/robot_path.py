def robot_path(destination_list):
	"""
	(list) -> boolean
	:param destination_list: a list containing the directions that robot passed
	:return: boolean 
	"""
	num_of_n = 0
	num_of_s = 0
	num_of_e = 0
	num_of_w = 0

	# The robot can only pass these two destinations
	# ["e", "n", "e", "e", "n"],
	# ["w", "n", "w", "n", "w", "w", "n"]

    # we can explain that robot goes to the east for 3 times and north for 2 times in destination NO. 1
	east_count_des1 = 3
	north_count_des1 = 2

	# we can explain that robot goes to the north for three times and north for 4 times in destination NO. 2
	north_count_des2 = 3
	west_count_des2 = 4

	# obtaining the number of direction the robot pass to arrive the specified destination
	for direction in destination_list:
		if direction == "n": num_of_n += 1
		elif direction == "s": num_of_s += 1
		elif direction == "e": num_of_e += 1
		elif direction == "w": num_of_w += 1

	if (num_of_n == north_count_des1 and num_of_e == east_count_des1) or (
			num_of_w == west_count_des2 and num_of_n == north_count_des2):
		return True
	else:
		return False

robot_path(["w", "n", "w", "n", "w", "w"])
