# Given a roman numeral as input, write a function that converts the roman
# numeral to a number and outputs it.
#
# Ex:
# translateRomanNumeral("LX") # 60
#
# When a smaller numeral appears before a larger one, it becomes
# a subtractive operation. You can assume only one smaller numeral
# may appear in front of larger one.
#
# Ex:
# translateRomanNumeral("IV") # 4
#
# You should return `nil` on invalid input.
#import roman

def get_user_input():
    str_input = raw_input("Enter a roman number: ")
    while str_input == "":
        str_input = raw_input("You can't have a blank input, Please Enter a roman number:  ")
    else:
        return str_input.strip()

def convert_to_roman(user_input):
    #create a dictionary of keys as the string roman and values as their respective data
    values = {"i":1, "v":5, "x":10, "l":50, "c":100, "m":1000}
    #sum the instance of each character found in user input based on the key, use a anonymous func
    return sum(map(lambda x: values[x], user_input))
print(convert_to_roman(get_user_input().lower()))
