def age_classifier(age):
    '''
    (int) -> str
    :param age:
    :return: The string including user age based on the user age
    '''
    result = ""
    if age <= 1:
        result = "infant"
    elif age < 13:
        result = "child"
    elif age < 20:
        result = "teenager"
    else:
        result = "adult"
    return f"According to your age, You are {result}"

user_input = int(input("Enter a person's age: "))
print(age_classifier(user_input))

