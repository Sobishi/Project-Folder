print("Let's Play!")

import random
#create two variables for user and computer
user_wins = 0
computer_wins = 0

choice = ["rock", "paper", "scissors"]

while True:
    user_input = input("choose between Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break

    if user_input not in choice: #Checking if the user typed in any of the words not in the list
        continue #continue asking until they type in the right word

    #create computer input

    random_num = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_input = choice[random_num]
    print("computer chose", computer_input + ".")

    #To determine who won
    if user_input == "rock" and computer_input == "scissors":
        print("you won!")
        user_wins += 1

    elif user_input == "paper" and computer_input == "rock":
        print("you won!")
        user_wins += 1
    

    elif user_input == "scissors" and computer_input == "paper":
        print("you won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("CPU won", computer_wins, "times.")
print("Thanks for playing")
   





