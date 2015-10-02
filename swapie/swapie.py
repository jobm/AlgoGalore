#Using python, have the function SwapCase(str) take the str parameter
#and swap the case of each character.
#For example: if str is "Hello World" the output should be hELLO wORLD.
#Let numbers and symbols stay the way they are.

#NB do not use the swapcase python method.
def SwapCase(string):
    rev_case = []
    for i in string:
        if i.isupper():
            rev_case.append(i.lower())
        elif i.islower():
            rev_case.append(i.upper())
        else:
            rev_case.append(i)
    print ''.join(rev_case)
def swapCase(string):
    #the join method is iterable
    return ''.join([char.upper() if char.islower() else char.lowwer() for char in string])

print(SwapCase("Hello World"))
print(swapCase("Beer Is So Sweeet"))

