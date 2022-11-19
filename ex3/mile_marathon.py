def multi_division(a, b, c):
    a = a * b
    if a % c == 0:
        return True
    else:
        return False


print(multi_division(42, 5, 10))