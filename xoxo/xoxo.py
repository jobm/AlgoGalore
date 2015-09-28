# Using Python, have the function xoxo(str) take the str parameter
# being passed and return the string true if there is an equal number of x's and o's,
# because you cannot recieve an uneven number of hugs and kisses :-)
# otherwise return the string false. Only these two letters will be entered in the string,
# no punctuation or numbers.
# For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.

def Xoxo(str):
  # code goes here
  x_count = 0
  o_count = 0
  for word in str:
      for w in word:
          if w == "x":
              x_count += len(w)
          elif w == "o":
              o_count += len(w)
  if x_count == o_count:
      return True
  return False
def Xoxo_simple(str):
    if str.count("x") == str.count("o"):
        return True
    return False
# keep the function call
print (Xoxo("have fun..xxxooox"))
print (Xoxo_simple("have fun..xxxooox"))
