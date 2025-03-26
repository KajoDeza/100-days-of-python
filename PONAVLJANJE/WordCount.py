def word_counter(sentence):
    words = sentence.split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

print(word_counter("Hello my name is Mark What is your name"))


