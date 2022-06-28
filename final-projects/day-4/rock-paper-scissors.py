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

#Write your code below this line 👇
choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if choice == "0":
  print(rock)
elif choice == "1":
  print(paper)
elif choice == "2":
  print(scissors)

print("Computer chose:\n")
computer_options = ["rock", "paper", "scissors"]

option_length = len(computer_options) - 1
random_option = random.randint(0,option_length)
print(random_option)

if random_option == 0:
  print(rock)
elif random_option == 1:
  print(paper)
elif random_option == 2:
  print(scissors)

if choice == "0" and random_option == 1:
  print("Paper beats Rock, you lose.")
elif choice == "0" and random_option == 2:
  print("Rock beats Scissors, you win!")
elif choice == "0" and random_option == 0:
  print("Tied Game.")
elif choice == "1" and random_option == 0:
  print("Paper beats Rock, you win")
elif choice == "1" and random_option == 1:
  print("Tied Game.")
elif choice == "1" and random_option == 2:
  print("Scissors beats Paper, you lose.")
elif choice == "2" and random_option == 0:
  print("Rock beats Scissors, you lose.")
elif choice == "2" and random_option == 1:
  print("Scissors beats Paper, you win!")
elif choice == "2" and random_option == 2:
  print("Tied Game.")
else:
  print("You typed an invalid number, you lose!!")