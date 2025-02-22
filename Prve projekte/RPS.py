import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("Welcome to the Rock & Paper & Scissors game! Are you ready to play! ")
the_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper and '2' for Scissors "))
if the_choice >= 0 and the_choice <= 2:
 print(game_images[the_choice])

computer_choice = random.randint(0, 2)
print("The computer chose:")
print(game_images[computer_choice])

if the_choice >= 3 or the_choice < 0:
      print("You typed an invalid number!")
elif the_choice == 0 and computer_choice == 2:
    print("You win! Congrats!")
elif computer_choice == 0 and the_choice == 2:
        print("You lose!")

elif computer_choice > the_choice:
    print("You lose :( ")
elif the_choice > computer_choice:
    print("You win")
elif computer_choice == the_choice:
    print("It's a draw")




