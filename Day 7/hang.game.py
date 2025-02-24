import random

word_list = ["Moon", "Life", "Psithurism", "Anaconda"]

chosen_word = random.choice(word_list)
print(chosen_word)

the_guess = input("Guess a letter: ").lower()
print(the_guess)

for letter in chosen_word:
    if letter == the_guess:
        print("Right")
    else:
        print("Wrong")