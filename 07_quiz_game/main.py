print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() == "no":
    print("Okay, maybe next time! 😔")
    quit()  # quit() is a built=in function that quits a code.
elif playing.lower() == "yes":
    print("Okay!, Let's play 😊")
else:
    print("Please answer with 'yes' or 'no'.")
    quit()

score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")

if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input(
    "What does RAM stand for? "
).lower()  # another method for converting the string.

if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} question(s) correct!")
print(f"You got {(score / 3) * 100:.2f}% correct!")
