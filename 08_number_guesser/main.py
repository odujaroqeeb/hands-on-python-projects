import random

range_limit = int(input("Type a number: "))

if range_limit <= 0:
    print("Please type a number larger than zero.")
    quit()


random_number = random.randrange(0, range_limit)  # one argument can be passed.

guesses = 0

while True:
    guesses += 1
    user_guess = int(input("Make a guess: "))

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You're above the number.")
    else:
        print("You're below the number.")

print(f"You got it in {guesses} guess(es)")

# random.randint(-5, 11)
