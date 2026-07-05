username = "admin"
password = "python123"

user = input("Enter your username: ")
pass_key = input("Enter your password: ")

if user == username and pass_key == password:
    print("Login successful!🚀")
elif user != username and pass_key == password:
    print("Username does not exist!❌")
elif user == username and pass_key != password:
    print("Incorrect password!❌")
else:
    print("These credentials don't match our record!❌")
