'''
 1 for rock 
-1 for paper
 0 for scissors

'''

import random

while True:


    computer = random.choice ([-1, 1, 0])
    youstr = input("Enter your choice: ")

    # Create a dictionary
    youDict = {'r': 1, 'p': -1, 's': 0}
    reverseDict = {1: 'rock', -1: 'paper', 0: 'scissors'}
    you = youDict[youstr]
    print(f" you choose {reverseDict[you]} \n computer choose {reverseDict[computer]}")

    # If user and computer has same choice

    if(computer == you):
        print("its a Draw")
    else:

        # If user select paper and computer select rock
        if(computer == 1 and you == -1):
            print("You win!")

            # If user select scissor and computer select paper
        elif(computer == -1 and you == 0):
            print("You win!")

            # If user select rock and computer select scissor
        elif(computer == 0 and you == 1):
            print("You win!")

            # If user select rock and computer select paper
        elif(computer == -1 and you == 1):
            print("You lose!")

            # If user select rock and computer select scissor
        elif(computer == 1 and you == 0):
            print("You lose!")

            # If user select paper and computer select scissor
        elif(computer == 0 and you == -1):
            print("You lose!")
            #If user selects the invalid option
        else:
         print("Something went wrong!")

        again = input("play again? (y/n): ")
        if again.lower() != "y":
            print(" thanks for playing!")
            break

        