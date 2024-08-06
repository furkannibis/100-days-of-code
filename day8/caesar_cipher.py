from string import ascii_letters, digits, punctuation
from art import logo

def encrypt(message, shift):
    all_chars = ascii_letters + digits + punctuation + ' ' + 'ßıçüöğşİÇÜÖĞŞ'
    encrypted_msg = ''
    for msgChar in message:
        if msgChar not in all_chars:
            msgChar += encrypted_msg
        char_index = all_chars.index(msgChar)
        new_char_index = (char_index + len(all_chars) + int(shift)) % len(all_chars)
        new_char = all_chars[new_char_index]
        encrypted_msg += new_char
    print(f'Here\'s the encoded result: {encrypted_msg}')

def decrypt(message, shift):
    all_chars = ascii_letters + digits + punctuation + ' ' + 'ßıçüöğşİÇÜÖĞŞ'
    all_chars = all_chars[::-1]
    decrypted_msg = ''
    for msgChar in message:
        if msgChar not in all_chars:
            msgChar += decrypted_msg
        char_index = all_chars.index(msgChar)
        new_char_index = (char_index + len(all_chars) + int(shift)) % len(all_chars)
        new_char = all_chars[new_char_index]
        decrypted_msg += new_char
    print(f'Here\'s the decoded result: {decrypted_msg}')

print(logo)

still_continue = True
while still_continue:
    guess = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n').lower()
    message = input('Type your message:\n')
    shift = input('Type the shift number:\n')

    if guess == 'encode':
        encrypt(message=message, shift=shift)
    elif guess == 'decode':
        decrypt(message=message, shift=shift)
    else:
        print('Invalid option!')
    
    if input('Type \'yes\' if you want to go again. Otherwise type \'no\': ').lower() != 'yes':
        still_continue = False