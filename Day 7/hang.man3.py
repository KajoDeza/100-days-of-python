import random

word_list = ["Moon", "Life", "Psithurism", "Anaconda"]

chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word)

placeholder = ""
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    the_guess = input("Guess a letter: ").lower()
    print(the_guess)

    display = ""

    for letter in chosen_word:
        if letter == the_guess:
            display += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")