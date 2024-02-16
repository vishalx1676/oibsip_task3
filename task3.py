import random
import string

def generate_password(length=12, include_letters=True, include_numbers=True, include_symbols=True):
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character set must be included.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Get user input for character set preferences
    include_letters = input("Include letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, include_letters, include_numbers, include_symbols)

    if password:
        print("Generated Password:", password)
    else:
        print("Password generation failed.")

if __name__ == "__main__":
    main()
