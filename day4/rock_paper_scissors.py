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

items = [rock, paper, scissors]

choose = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if choose >= 3 or choose < 0:
    print('You typed invalid number, you lose!')
else:
    print(items[choose])

    print('Computer chose:')
    comp_choose = random.randint(0, 2)
    print(items[comp_choose])


    if choose == 0 and comp_choose == 2:
        print('You wins!')
    elif choose == 2 and comp_choose == 0:
        print('You lose!')
    elif comp_choose > choose:
        print('You lose!')
    elif choose > comp_choose:
        print('You win!')
    elif comp_choose == choose:
        print('It\'s a draw!')

