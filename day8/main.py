def greet():
    print('Hello')
    print('How do you do?')
    print('Isn\'t the weather nice?')

greet()

def greet_with_name(name):
    print(f'Hello {name}')
    print(f'How do you do {name}?')

greet_with_name('Furkan')

def greet_with_name_location(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')

greet_with_name_location(name='Furkan', location='Ankara')
greet_with_name_location(name='Emre', location='Istanbul')