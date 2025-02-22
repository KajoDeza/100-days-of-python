print("Welcome to our rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height < 160:
    print("You cannot ride the collercoaster!")

else:
    print("You can ride the rollercoaster")

age = int(input("What is your age? "))

if age <= 12:
    bill = 5
    print("Child tickets cost $5")

elif age <=18:
    bill = 8
    print("Young teenagers tickets cost $8")

else:
    bill = 10
    print("Adult tickets cost $10")

the_photo = input("Do you want to have a photo taken? Type Y for yes or N for no ")
if the_photo == "Y":
    bill += 3
    print(f"Your final bill is: {bill} dollars")