import random

top_range = input("Enter a number: ")

if top_range.isdigit():
    top_range = int(top_range) #converts digit to integer

    if top_range <= 0: #checks if number is greater than 0
        print("Please enter a number greater than 0")
        quit()
else:
    print("Please type a number next time") #checks if a number was entered by the user
    quit()

random_number = random.randint(0, top_range) #calls bottom of the range 0, and top_range variable
number_of_guess = 0 #checking the number of times the user made a guess.
while True:
    number_of_guess += 1
    user_guess = input("Make a guess: ") #user inputs a guess
    if user_guess.isdigit(): #checks if the user entered an actual number
        user_guess = int(user_guess) #converts str of number to an integer
    else:
        print("please type a number next time")
        continue #take us back and asks user to make another guess

    if user_guess == random_number:
        print("you got the right answer!")
        break #to stop once user guesses the right answer

    elif user_guess > random_number:
            print("you were above the number")
    else:
        print("you were below the number")

print("You got it in", number_of_guess, "guesses")
    