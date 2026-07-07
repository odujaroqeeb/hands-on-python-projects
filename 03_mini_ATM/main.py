balance = 5000

print("Pick a service in the menu below")
print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter choice: "))

if choice == 1:
    print(f"Your balance is: {balance}")

elif choice == 2:
    deposit = int(input("Deposit amount: "))

    if deposit > 0:
        balance += deposit
        print("Deposit successful!")
        print(f"Your new balance is: {balance}")
    else:
        print("Invalid amount")

elif choice == 3:
    amount = int(input("Withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount")

    elif amount > balance:
        print("Insufficient balance")
        print(f"Your balance is: {balance}")
    else:
        balance -= amount
        print("Withdrawal successful!")
        print(f"Your new balance is: {balance}")
else:
    print("Invalid choice input")
