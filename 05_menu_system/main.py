print("Hello!, Welcome to your menu system.")

name = input("Enter your name? ")

print(f"Hello! {name}")

menu = ["1. Say Hello", "2. Tell a joke", "3. Exit"]

while True:
    for i in menu:
        print(i)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Hello!!!!")
        print()  # To leave a space between the output and the menu
    elif choice == 2:
        print("A fool will laugh when nothing is funny.")
        print()  # To leave a space between the output and the menu
    elif choice == 3:
        print(f"Thank you {name} for using the menu system. Goodbye!")
        break
    else:
        print("Invalid input")
