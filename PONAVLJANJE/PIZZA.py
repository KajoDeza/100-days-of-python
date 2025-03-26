print("Welcome to: HOW WOULD YOU LIKE YOUR PIZZA! ")

bill = 0

large_pizza = 20
medium_pizza = 15
small_pizza = 10
size = input("What size would you like your pizza? Large, Medium or Small?  ").lower()

if size == 'Large':
  the_pizza = bill + large_pizza
elif size == 'Medium':
    the_pizza = bill + medium_pizza
else:
    the_pizza = bill + small_pizza
print(f"Your pizza costs: {the_pizza} $")
