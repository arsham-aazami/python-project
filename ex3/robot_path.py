def robot_path(direction_list):
	
	distance = 0
	for direction in direction_list:
		if direction == "n":
			distance += 1
		elif direction == "s":
			distance -= 1
		elif direction == "e":
			distance += 2
		elif direction == "w":
			distance -= 2
	return distance


c = robot_path(['e', 'e', 'w', 'n', 'n', 'n'])
print(c)
