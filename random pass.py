import random
import string

def password(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = "".join(random.choice(characters) for i in range(length))
    return password

# Ask the user for the desired length of the password
password_length = int(input("Enter the length of the password: "))

# Generate and print the password
print("Generated Password:", password(password_length))
