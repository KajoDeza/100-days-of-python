import random

secret_number = random.randint(1, 51)
attempts = 0

while True:
    number = int(input("Guess a number between 1 and 50: "))
    if number > secret_number:
        print("The number is too high.")
        attempts += 1
    elif number < secret_number:
        print("The number is too low.")
        attempts += 1
    elif number == secret_number:
        print("Well done! You have guessed the correct number.")
        break