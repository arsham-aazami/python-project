def collatz_conjecture(number):
	"""
    (int) -> int
    :param number:
    :return: the number of steps that repeatedly performed
    """

	num_of_step = 0

	if number > 0:
		while number != 1:
			if number % 2 == 0:
				number /= 2
			else:
				number *= 3
				number += 1
			num_of_step += 1
	else:
		return "Oops! you should enter a positive number"
	return num_of_step


print(collatz_conjecture(10))
