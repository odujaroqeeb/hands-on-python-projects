name = input("Enter your name: ")
print(f"Welcome {name} to this adventure!.")
print()

answer = input(
    "You are on a dirt road, \nit has come to an end and you can go left or right. \nEnter which way you would like to go: "
).lower()

print()

if answer == "left":
    answer = input(
        "You come to a river, \nyou can walk around it or swim across. \nType 'walk' to walk around and 'swim' to swim across: "
    ).lower()

    print()

    if answer == "swim":
        print("You swam across and you were eaten by an alligator. \n You lose!")
    elif answer == "walk":
        print("You walked for many miles, \nran out of water, \nand You lose!.")
    else:
        print("Not a valid option, \nYou lose!.")

elif answer == "right":
    answer = input(
        "You come to a bridge, \nit looks wobbly, \nEnter 'cross' to cross it or 'back' to head back: "
    ).lower()

    print()

    if answer == "back":
        print("You go back and you lose!.")
    elif answer == "cross":
        answer = input(
            "You cross the the bridge and meet a stranger. \nDo you talk to them? "
        ).lower()

        print()

        if answer == "yes":
            print("You talk to the stranger and they give you. \nCongrats, You win!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and \nYou lose!.")
        else:
            print("Not a valid option, \nYou lose!.")
    else:
        print("Not a valid option, \nYou lose!.")

else:
    print("Not a valid option, \nYou lose!.")

print(
    f"Thank you {name} for playing CHOOSE YOU OWN ADVENTURE, We'll love to have you again."
)
