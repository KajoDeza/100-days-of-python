
print("Welcome to the BMI calculator!")

weight = int(input("What is your weight in kg? "))
print("Okay")

height = float(input("What is your height in cm? "))
print("Got it!")

bmi = weight / (height ** 2)
print(bmi)

if bmi < 18.5:
    print("Underweight")

elif bmi >= 18.5 and bmi  <= 25:
    print("Normal weight")

elif bmi >= 25 and bmi <= 30:
    print("Overweight")

else:
    print("Obesity")