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

import random as rd
hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
randhand = rd.randint(0,2)
counter = hand - rd.randint(0, 2)  

if hand == 0:
  print(f"0 \n{rock}")
elif hand == 1:
  print(f"1 \n{paper}")
elif hand == 2:
  print(f"2 \n{scissors}")
else: 
  hand = randhand
  print(f"You're confused. \nAccidentally put {hand}. \n ")
  if hand == 0:
    counter = 1
    print(f"\n{rock}")
  elif hand == 1:
    counter = 2
    print(f"\n{paper}")
  elif hand == 2:
    counter = 0
    print(f"\n{scissors}")
  

print("Computer choose: ")
if counter == 0:
  print(f"0 \n{rock}")
elif counter == 1:
  print(f"1 \n{paper}")
elif counter == 2:
  print(f"2 \n{scissors}")

if hand == 0 and counter == 0:
  print("Draw~")
elif hand == 0 and counter == 1:
  print("You lost..")
elif hand == 0 and counter == 2: 
  print("You've triumph!")
elif hand == 1 and counter == 1:
  print("Draw~")
elif hand == 1 and counter == 2:
  print("You lost..")
elif hand == 1 and counter == 0: 
  print("You've triumph!")
if hand == 2 and counter == 2:
  print("Draw~")
elif hand == 2 and counter == 0:
  print("You lost..")
elif hand == 2 and counter == 1: 
  print("You've triumph!")
  
# see how this runs on replit: https://replit.com/@Hertzspr/rock-paper-scissors-punish#main.py
