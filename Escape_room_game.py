player1 = input("Enter your name to start your adventure: ")
print("Welcome to escape room game", player1)

answer = input("You have entered the escape room, type 'left' or 'right' to find your way out: ")
if answer == "left":
    answer = input("You are in a dark room filled with ice, you have only two switches for heater to keep warm or light to see (heater or light?): ")
    if answer == "heater":
        print("keep warm till you get trapped!, Game over")
    elif answer == "light":
        answer = input("You turned on the light you are able to see the door and found a key, type 'up' to pick up the key or 'ignore' to keep looking: ")
        if answer == "up":
            answer = input("Door opened, you are at a parking lot, type 'start' to move a car or 'wave' to stop a cab: ")
        elif answer == "ignore":
            answer = input("you keep looking until you find another door that leads to a gate, type 'push' to open the gate or 'jump' to climb over: ")
            if answer == "push":
                answer = input("Gate opens and you arrive at a parking lot, type 'drive' to move the car or 'cab' to use a taxi service: ")
                if answer == "drive":
                    answer == input("you have escaped from the parking lot and approaching the game police, type 'talk' to have a conversation or 'run' to clear the roadblock: ")
            elif answer == "climb":
                print("you landed in front of lion in a desert and got eaten up, game over!")
elif answer == "right":
    answer = input("You met a stranger in the room, type 'yes' to talk or 'no' to ignore: ")
    if answer == "yes":
        answer = input("You spoke to stranger and got direction to the next room, type 'left' to follow stranger or 'right' to keep going your way: ")
        if answer == "left":
            print("you followed stranger to a dead end!, Game over")
        elif answer == "right":
            answer = input("you met a warewolf, type 'weapon' to fight, or type 'run' to escape:")
            if answer == "weapon":
                answer = input("You struck the warewolf and got challenged by its mother, type 'weapon' to keep fighting or 'run' to escape: ")
        elif answer == "run":
            print("you ran and got caught!, game over!")
    elif answer == "no":
        print ("You ignored the stranger and got trapped!, game over!")
        

