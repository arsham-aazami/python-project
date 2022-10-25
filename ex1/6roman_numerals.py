def roman_numerals(number):
    '''
    (int) -> str
    :param number:
    :return: The numeral version of the numbers within the range of 1 through 10
    '''
    roman_numerals_dic = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
    }
    if 1 <= number <= 10:
       return roman_numerals_dic[number]
    else:
        return "Error: number is less than 1 or greater than 10"


input_number = int(input("Enter a arbitrary number: "))
print(roman_numerals(input_number))
