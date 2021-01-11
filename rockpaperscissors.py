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

userChoise = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if userChoise == "0":
  print(rock)
elif userChoise == "1":
  print(paper)
elif userChoise == "2":
  print(scissors)

print("Computer Chose:")

computerChoise = random.randint(0, 2)

if computerChoise == 0:
  print(rock)
elif computerChoise == 1:
  print(paper)
elif computerChoise == 2:
  print(scissors)

if int(userChoise) == computerChoise:
  print("Its a draw")

if userChoise == "0":
  if computerChoise == 1:
    print("You Lose")
  if computerChoise == 2:
    print("You Win")

if userChoise == "1":
  if computerChoise == 0:
    print("You Win")
  if computerChoise == 2:
    print("You Lose")

if userChoise == "2":
  if computerChoise == 0:
    print("You Lose")
  if computerChoise == 1:
    print("You Win")
