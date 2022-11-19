def collatz_conjecture(number):
    """
    """
    num_of_step = 0

    for num in range(number,0, -1):
        if num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num *= 3 
                num += 1 
        else:
            return "Oops! you should enter a positive number"
        step += 1

print(collatz_conjecture(3))



if num