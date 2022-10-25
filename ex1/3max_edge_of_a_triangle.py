def max_edge_of_a_triangle(side1, side2):
    '''

    :param side1:
    :param side2:
    :return: The maximum value of the third side of the triangle
    based on the other two sides
    '''
    maximum_third_side = (side1 + side2) - 1
    return maximum_third_side

side3_1 = max_edge_of_a_triangle(23, 12)
side3_2 = max_edge_of_a_triangle(23, 12)
print(side3_1, side3_2)