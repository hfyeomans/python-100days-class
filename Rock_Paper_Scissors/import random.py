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



