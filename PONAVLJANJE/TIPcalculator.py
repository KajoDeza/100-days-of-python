print("Welcome to the TIP calculator!")

the_bill = int(input("What was the total bill:\n $"))
tip = int(input("How much tip would you like to give?\n$ "))
people = int(input("How many people will split the bill?"))

total_bill = the_bill / people
print(f"You have to pay: {total_bill} $")

the_bill_and_tip = total_bill + tip
print(f"If you gave a tip you'll have to pay: {the_bill_and_tip}")
