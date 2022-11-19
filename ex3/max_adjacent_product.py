def max_adjacent_product(list):
    '''
        (list) -> int
        :param list: a list of integers
        :return: the maximum adjance product(int)
	'''
    product_list = []

    for index in range(len(list) - 1):
        product_result = list[index] * list[index + 1] 
        product_list.append(product_result)

    max_product = max(product_list)
    return max_product
res = max_adjacent_product([3, 6, -2, -5, 7, 3])
print(res)

