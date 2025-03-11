role = input("Enter your role please:\nadmin\neditor\nviewer\n").lower()

if role == "admin":
    print("Welcome, admin! You have full access")
elif role == "editor":
    print("Welcome, editor! You can edit content")
elif role == "viewer":
    print("Welcome, viewer! You can only view content")
else:
    print("Access denied")
