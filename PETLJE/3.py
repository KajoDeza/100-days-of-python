
total = 0
add_numbers = True

while add_numbers:
    the_num = int(input("Enter a number you like: "))
    if the_num <= 0:
        break
    total += the_num

print(f"The sum of the numbers is: {total}")




