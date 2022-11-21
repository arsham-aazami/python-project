def face_interval(int_list):
    """
    ([int]) -> str
    :param int_list: a list of integers
    :return: ":)" if the interval is equal to any other number in the list otherwise returns ":("
    """
    interval = max(int_list) - min(int_list)
    face = ""
    for number in int_list:
        if number == interval:
            face = ":)"
        else:
            face = ":("
    return face


face_interval([2, 32, 1, 6, 31])
