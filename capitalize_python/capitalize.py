# Using ruby, have the function capitalize(str) take the str parameter being passed and capitalize
# the first letter of each word. Words will be separated by only one space.
# it should take string input from a user
# do not use the capitalize method
def get_user_input():
    str_input = raw_input("Enter a sentence: ")
    while str_input == "":
        str_input = raw_input("Enter a sentence: ")
    else:
        print(capitalizer(str_input))
def capitalizer(str_input):
    list_words = str_input.split( )
    list_split = []
    for word in list_words:
       list_split.append(word.replace(word[0],word[0].upper()))
    return ' '.join(list_split)
get_user_input()
