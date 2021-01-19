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


#Get input
your_choice = input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors\n")
# The choices you can make
choices = [rock, paper, scissors]
choices_len = len(choices)
# The computer choices
random_choice = random.randint(0, choices_len)
# Change to an integer
your_choice = int(your_choice)
# Get the choice and adjust for index
random_choice = random_choice -1
#The computer chose
print(choices[random_choice])
print("Computer chose:")
# User wins if true
print(choices[your_choice])
# catch other numbers


while True:
  if choices[your_choice] == choices[0] and choices[random_choice] == choices[2]:
    rock_you_win = True
    print("You win!")
  elif not choices[your_choice] == choices[0] and choices[random_choice] == choices[2]:
    rock_you_win = False  
    print("You lose!")
  else:
    rock_you_win = "tie"
    print("It's a tie try again!")
    break

  if choices[your_choice] == choices[1] and choices[random_choice] == choices[0]:
    paper_you_win = True
    print("You win!")
  elif not choices[your_choice] == choices[1] and choices[random_choice] == choices[0]:
    paper_you_win = False
    print("You lose!")
  else:
    paper_you_win = "tie"
    print("It's a tie try again!")
    break
  if choices[your_choice] == choices[2] and choices[random_choice] == choices[1]:
    scissors_you_lose = True
    print("You win!")
  elif not choices[your_choice] == choices[2] and choices[random_choice] == choices[1]:
    scissors_you_lose = False
    print("You lose!")
  else:
    scissors_you_win = "tie"
    print("It's a tie try again!")
    break
