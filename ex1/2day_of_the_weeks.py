def day_of_the_weeks(day):
    user_input = input("Type a number between 1 and 7")
    # using dictionary to assign the integer number to the days of a week
    week_day={
        1:"monday",
        2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday",
        6: "saturday",
        7: "sunday"
    }
    return week_day[f"{user_input}"]


day1 = day_of_the_weeks(1)
day2 = day_of_the_weeks(5)
print(day1, day2)