# Simple Password Generator

import random
import string

# Ask the user for the desired password length
length = int(input("Enter the desired password length: "))

# Combine all possible characters: letters, digits, and symbols
all_characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password by picking random characters
password = ""
for i in range(length):
    password = password + random.choice(all_characters)

# Display the generated password
print("Generated Password:", password)