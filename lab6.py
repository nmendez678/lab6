# user menu selection
def menu():
    print('Menu\n-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


# Encodes password
def encode(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


# Decodes password
# Paula Morales Rivera Decoder
def decode(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

def main():
    while True:
        menu()
        option = int(input('\nPlease enter an option: '))
        
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!\n')
        # Paula Morales Decoder
        elif option == 2:
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.\n')
        elif option == 3:
            break
        


if __name__ == '__main__':
    main()
