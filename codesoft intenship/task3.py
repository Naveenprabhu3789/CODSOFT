import random
import string

def generate_password(length):
    # Define the character sets for different complexity levels
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine the character sets based on the desired complexity
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the length is at least 8 characters
    length = max(length, 8)

    # Generate the password using random.choices
    password = ''.join(random.choices(all_characters, k=length))

    return password

def main():
    print("Password Generator")

    try:
        # Prompt the user for the desired password length
        length = int(input("Enter the desired length of the password: "))

        # Generate and display the password
        password = generate_password(length)
        print("Generated Password: {}".format(password))

    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
