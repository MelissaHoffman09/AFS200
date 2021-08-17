#Odd or Even Project

number = input("Enter a number: ")
if int(number) % 4 == 0:

# Extra Credit 1 - if number is multiple of 4, print a different message 

    print("The number is a multiple of 4")
if int(number) % 2 == 0: 
    print("The number is even")
else:
    print("The number is odd")

# Extra Credit 2 - Ask user for two numbers, divide the 1st number provided by the 2nd to check if the 2nd divided against the 1st is even or not

num = input("Enter a number: ")
check = input("Enter a number to divide by: ")
answer = int(num) % int(check)
if answer == 0:
    print(check, "divides equally into", num)
else:
    print(check, "does not divide equally into", num)