def format_name(first_name, last_name):
    return f'{first_name} {last_name}'.title()

print(format_name('furkan', 'ibiş'))

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

print(f'{function_2(function_1("SomethinG"))}')

def format_name_2(first_name, last_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if first_name == '' or last_name == '':
        return 'You did not provide vali inputs'

    formatted_f_name = first_name.title()
    formatted_l_name = last_name.title()

    return f'Result: {formatted_f_name} {formatted_l_name}'

print(format_name_2(first_name=input('First name: '), last_name=input('Last name: ')))