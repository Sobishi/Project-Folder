print("Welcome to my quiz game!")

playing = input("Do you want to play?: ")
if playing.lower() != "yes":
    quit()
print("Game on! lets play :) ")
score = 0 #add score to each correct answer

answer = input("what does CPU stand for?: ")
if answer.lower() == "central processing unit":
    print("correct!, get ready for next question")
    score += 1
else:
    print("incorrect!")

answer = input("what does GPU stand for?: ")
if answer.lower() == "graphics processing unit":
    print("correct!, get ready for next question")
    score += 1
else:
    print("incorrect!")

answer = input("what does RAM stand for?: ")
if answer.lower() == "random access memory":
    print("correct!, get ready for next question")
    score += 1
else:
    print("incorrect!")

answer = input("what does LMAO stand for?: ")
if answer.lower() == "laugh my ass off":
    print("correct!, get ready for next question")
    score += 1
else:
    print("incorrect!")

answer = input("what does SMH stand for?: ").lower()
if answer.lower() == "shake my head":
    print("correct!, get ready for next question")
    score += 1
else:
    print("incorrect!")

print("You got" + " " + str(score) +" " + "questions correct!")
