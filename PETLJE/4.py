
the_correct_password = "1234"
the_password = True

while the_password:
    password = input("Enter the password: ")

    if password == the_correct_password:
        print("Correct password!")
        break
    else:
        print("Incorrect password. Please try again")
