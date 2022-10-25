def day_of_the_weeks(day):
    '''
    (int) -> str
    :param day:
    :return: The corresponding day of the week based on the input number
    where 1 = monday 2 = tuesday .... 7 = sunday
    '''
    # using dictionary to assign the integer number to the days of a week
    week_day={
        1: "monday",
        2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday",
        6: "saturday",
        7: "sunday"
    }
    return week_day[user_input]

#taking the user input
user_input = int(input("Type a number between 1 and 7: "))
if 1 <= user_input <= 7:
    specified_day = day_of_the_weeks(user_input)
    print(specified_day)
else:
    print("invalid number for a week day!")