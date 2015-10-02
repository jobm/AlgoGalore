# Using Python, have the function Secondy(lis) take the list of numbers stored in lis
# and return the second lowest and second greatest numbers, respectively, separated by a space.
# For example: if lis contains [7, 7, 12, 98, 106] the output should be 12 98.
# The list will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers!

def Secondy(lis):
    lis.sort()
    list_wanted = []
    list_wanted.append(lis[len(lis)-1])
    list_wanted.append(lis[len(lis)-2])
    return list_wanted

# keep this function call below here
print Secondy([100,20,4,1,11500])
