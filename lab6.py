# encode password
def encode(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

# loop
while True:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

    # User menu selection
    op = int(input('Please enter an option: '))

    # Perform selected operation
    if op == 1:
        password = input('Please enter your password to encode: ')
        encoded_password = encode(password)
        print('Your password has been encoded and stored!\n')
    elif op == 2:
        pass
    elif op == 3:
        break
