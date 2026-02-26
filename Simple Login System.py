# Simple Login System

stored_username = "admin"
stored_password = "1234"

print("=== Welcome to the Login System ===")

attempts = 3   

while attempts > 0:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == stored_username and password == stored_password:
        print("Login Successful! Welcome,", username)
        break
    else:
        attempts -= 1
        print("Incorrect username or password.")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account locked! Too many failed attempts.")
