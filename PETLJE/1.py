grade = int(input("What score did you get on your maths exam? "))

if grade > 89 < 100:
    print(f"{grade} A")
elif grade > 79 < 90:
    print(f"{grade} B")
elif grade > 69 < 80:
    print(f"{grade} C")
elif grade > 59 < 70:
    print(f"{grade} D")
elif grade < 60:
    print(f"{grade} F")
