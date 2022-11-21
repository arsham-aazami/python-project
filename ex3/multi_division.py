def multi_division(a, b, c):
    """
        (int, int, int) -> boolean
        :param a:
        :param b:
        :param c:
        :return: A boolean if "a" time "b" is divisible by "c" function returns True otherwise returns False
    """

   
    for i in range(b):
        a *= 2 
    print(a)

    if a % c == 0:
        return True
    else:
        return False


multi_division(42, 5, 10)


