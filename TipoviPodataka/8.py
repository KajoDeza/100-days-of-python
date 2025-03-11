the_first_nnumber = int(input("Enter the first number please: "))
print("+ \n - \n * \n / \n ")
operator = input("Choose an operator: ")
the_second_number = int(input("Enter the second number please: "))

if operator == "+":
    print(the_first_nnumber + the_second_number)
elif operator == "-":
    print(the_first_nnumber - the_second_number)
elif operator == "*":
    print(the_first_nnumber * the_second_number)
elif operator == "/":
    print(the_first_nnumber / the_second_number)
else:
    print("You entered an invalid operator")
