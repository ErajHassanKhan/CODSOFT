import random
import string

while True:
    try:
        user_input = input("Enter the desired password length (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            break  
        
        length = int(user_input)
        
        if length < 1:
            print("Password length should be at least 1.")
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")
