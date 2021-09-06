 # Python Lambda
 # Create a function that takes one argument, 
 # and that argument will be multiplied with an unknown given number

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(5)

print(mydoubler(8))