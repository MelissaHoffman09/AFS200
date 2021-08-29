import random
num_random = random.randint(1, 9)
exit = False
count = 0
while exit is False:
    num_guess = int(input("Guess a number between 1 and 9: "))
    if num_random < num_guess:
        print("Your number is too high")
        count += 1
    elif num_random > num_guess:
        print("Your number is too low")
        count += 1
    elif num_random == num_guess:
        print("Correct! You guessed it right!")
        count += 1
        print("Guess Count:", count)
        break
    exit = input("Press enter to continue or type exit: ")
    if exit == "exit":
        print("Total Guess Count:", count)
        exit = True
    elif exit != "exit":
        exit = False