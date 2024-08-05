import string
import random

print('Welcome to the PyPassword Generator!')
usr_letter = int(input('How many letters would you like in your password?\n'))
usr_symbol = int(input('How many symbols would you like?\n'))
usr_number = int(input('How many numbers would you like?\n'))

letters = random.choices(string.ascii_letters, k=usr_letter)
symbols = random.choices(string.punctuation, k=usr_symbol)
numbers = random.choices(string.digits, k=usr_number)

pass_list = letters + symbols + numbers
random.shuffle(pass_list)

print(f'Here is your password: {"".join(pass_list)}')