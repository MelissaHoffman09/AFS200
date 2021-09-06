# Python Functions
# Accept a string and calculate the number of upper case letters and lower case letters.

def case(s):      
    upper = sum(1 for i in s if i.isupper())
    lower = sum(1 for i in s if i.islower())
    print( "No. of Upper case characters : %s , No. of Lower case characters : %s" % (upper,lower))

case("ZEN OF PYTHON: Beautiful is better than ugly. Explicit is better than implicit.")