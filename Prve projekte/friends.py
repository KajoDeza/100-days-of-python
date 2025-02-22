import random

friends = ["Alice", "John", "Anne", "Khaled", "Emily"]

print(random.choice(friends))
# Option2
random_index = random.randint(0, 4)
print(friends[random_index])

print("Hi!")


