from collections import OrderedDict
def removeDuplicates(string):
    lis = list(OrderedDict.fromkeys(string))
    return ''.join(lis)
print(removeDuplicates("tree traversal"))