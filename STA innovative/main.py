print("====== LOGIN SYSTEM ======")

username = input("Enter Username : ")
password = input("Enter Password : ")

saved_username = "admin"
saved_password = "admin123"

attempts = 3

for i in range(attempts):

    print("\nChecking Login Details...")

    if username == saved_username:
        print("Username Found")
        
        if password == saved_pass:

            print("Password Correct")
            print("Login Successful")

            print("Welcome to Dashboard")
            print("Loading User Data...")
            print("Access Granted")

            break

        else:
            print("Wrong Password")

    else:
        print("Invalid Username")

    print("Attempts Left:", attempts - i - 1)

    username = input("Re-enter Username : ")
    password = input("Re-enter Password : ")

print("\nSystem Closed")
