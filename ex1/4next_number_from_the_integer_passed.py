
def return_the_next_number_from_integer_passed(number):
    '''
    (int) -> int
    :param number:
    :return: The number incremented by 1
    '''
    number = number + 1
    return number

result1 = return_the_next_number_from_integer_passed(1)
result2 = return_the_next_number_from_integer_passed(4)
print(result1, result2)