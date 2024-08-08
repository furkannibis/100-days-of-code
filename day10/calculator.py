from art import logo

def addition(number1, number2):
    print(f'{number1} + {number2} = {number1 + number2}')
    return number1 + number2

def subtraction(number1, number2):
    print(f'{number1} - {number2} = {number1 - number2}')
    return number1 - number2

def multiplication(number1, number2):
    print(f'{number1} * {number2} = {number1 * number2}')
    return number1 * number2

def division(number1, number2):
    print(f'{number1} / {number2} = {number1 / number2}')
    return number1 / number2

usr_continue = ''

operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}

print(logo)

while usr_continue != 'q':

    if usr_continue != 'y':
        number1 = float(input('What\'s the first number: '))
    else:
        number1 = result

    operation = input('+\n-\n*\n/\nPick an operation: ')
    number2 = float(input('What\'s the next number: '))

    result = operations[operation](number1=number1, number2=number2)

    usr_continue = input(f'Type \'q\' to exit or \'y\' to continue calculating with {round(result, 2)}, or type \'n\' to start a new calculation: ').lower()
    