import random
import datetime
import os

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    # Init variables
    total = 0
    amountOfRolls = 0

    # Ask how many times to roll
    rolls = input("Roll Die x Times: ")

    # Options for input
    if(rolls == "q" or rolls == "quit"):
        print("You have quit the program")
        exit()
    elif(rolls == "c" or rolls == "clear"):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Roll dice
    else:
        try:
            # Roll dice 'rolls' amount of times
            for x in range(0, int(rolls)):
                dice = random.randrange(1, 6, 1)
                total += dice
                amountOfRolls += 1
                print(dice)

            # Print results
            print()
            print(datetime.datetime.now())
            print("Your total roll =", total)
            print("Your average roll =", total/amountOfRolls)
            print()
            
        # Print this when there isn't a number entered
        except ValueError:
            print("Please enter a number")

        # Print other errors
        except Exception as e:
            print(e)