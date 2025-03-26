print("Welcome to the BMI calculator!")

the_height = float(input("Enter your height in cm please: "))
the_weight = int(input("Enter your weight please: "))

bmi = the_weight / the_height ** 2

print(f"Your BMI is: {bmi}")

the_bmi = True

while the_bmi:
    if bmi < 18.5:
        print("Underweight")
        quit()
    elif bmi >= 18.5 < 25:
        print("Normal weight")
        quit()
    elif bmi >= 25:
        print("Overweight")
        quit()
    else:
        print("Your input was not valid. Please try again. ")
        the_bmi = False