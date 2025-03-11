def count_vowels(text):
    vowels = "aeioyAEIOY"
    return sum(1 for char in text if char in vowels)

print(count_vowels("Diellza"))
