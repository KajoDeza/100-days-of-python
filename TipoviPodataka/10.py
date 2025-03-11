import random

random_numbers = random.randint(1, 10)
another_random = random.randint(1, 10)

the_result = float(input(f"What is the sum of {random_numbers} + {another_random} = "))

the_correct_answer = random_numbers + another_random

if the_result == the_correct_answer:
    print("CORRECT!".upper())
else:
    print("WRONG".upper())
