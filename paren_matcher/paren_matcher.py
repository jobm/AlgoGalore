# Write a function that return whether or not the input string has balanced parantheses
# Balanced:
#   '((()))'
#   '(()())'
# Not balanced:
#   '((()'
#   '())('
def balanced(parens):
    if parens.count("(") == parens.count(")"):
        return "balanced"
    return "Not balanced"
print(balanced("(())"))
