import string
import random


def uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False


def lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False


def digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def check_password_strength_option1(password):
    length = len(password)
    has_upper = uppercase(password)
    has_lower = lowercase(password)
    has_digit = digit(password)

    if length < 5:
        return "Very weak"
    elif 5 <= length <= 7 and (has_upper or has_lower or has_digit):
        return "Weak"
    elif 8 <= length < 10 and has_upper and has_lower and has_digit:
        return "Strong"
    elif length >= 10 and has_upper and has_lower and has_digit:
        return "Very strong"

def check_password_strength_option2(password):
    length = len(password)
    num_digits = sum(1 for char in password if char.isdigit())

    if length < 5:
        return "Very weak"
    elif 5 <= length <= 7:
        return "Weak"
    elif 8 <= length <= 10:
        return "Strong"
    else:
        return "Very strong"


def generate_random_password(length=12, num_digits=3):
    if length < 8:
        return "Error, Password must be at least 8 characters long."

    characters = string.ascii_letters + string.digits
    digits = string.digits

    password = ''.join(random.choice(characters) for _ in range(length - num_digits))
    password += ''.join(random.choice(digits) for _ in range(num_digits))

    return password


choice = input("Press 1 to enter your own password or 2 to generate a random password: ")

if choice == '1':
    while True:
        password = input("Enter a password: ")
        strength_result = check_password_strength_option1(password)
        if strength_result in {"Strong", "Very strong"}:
            print("Password strength:", strength_result)
            break
        else:
            print("Password is not strong enough. Please enter a stronger password.")

elif choice == '2':
    while True:
        try:
            num_digits = int(input("Enter the number of digits you want in the password: "))
            if num_digits < 0:
                print("Error, Number of digits cannot be negative.")
            elif num_digits < 8:
                print("Error, Number of digits cannot be less than 8.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

    password = generate_random_password(length = num_digits)
    strength_result = check_password_strength_option2(password)
    print("Generated random password:", password)
else:
    print("Invalid choice.")
    exit()
