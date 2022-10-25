def area_of_a_triangle(base,height):
    '''
    (int, int) -> int
    :param base:
    :param height:
    :return: Area of the specified triangle by using its base and height
    '''
    area = (base * height) / 2
    return area


area1 = area_of_a_triangle(40, 12)
area2 = area_of_a_triangle(32, 15)
print(area1, area2)