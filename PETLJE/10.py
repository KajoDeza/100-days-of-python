word = input("Enter a word you like: ")
reversed_word = ""

for letter in word:
    reversed_word = letter + reversed_word

print(f"The reversed word: {reversed_word}")
