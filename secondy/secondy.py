# Using Python, have the function Secondy(lis) take the list of numbers stored in lis
# and return the second lowest and second greatest numbers, respectively, separated by a space.
# For example: if lis contains [7, 7, 12, 98, 106] the output should be 12 98.
# The list will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers!

def Secondy(lis):
    lis.sort()    
    if lis[0] == lis[1]:
        return lis[2],lis[len(lis)-2]
    return lis[1], lis[len(lis)-2]
print Secondy([7, 7, 12, 98, 106])
