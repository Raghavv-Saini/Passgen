import random 
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits 
    special = string.punctuation

    charachters = letters
    if numbers:
        charachters += digits
    if special_characters:
        charachters += special

    pwd =""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(charachters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd        


min_length = int(input("Enter minimum password length: "))
has_numbers = input("Include numbers? (y/n): ").lower() == 'y' 
has_specials = input("Include special characters? (y/n): ").lower() == 'y' 
pwd = generate_password(min_length, has_numbers, has_specials)
print("Generated password:", pwd)