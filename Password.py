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


def special_char(password):
    special_characters = "!@#&"
    for char in password:
        if char in special_characters:
            return True
    return False


def check_password_strength(password):
    if len(password) < 8:
        return "Weak, Password should be at least 8 characters long."

    if not uppercase(password) or not lowercase(password) or not digit(password) or not special_char(password):
        return "Weak, Password should include uppercase, lowercase, digits, and special characters."

    return "Strong, Password is secure."


def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#&"

    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if uppercase(password) and lowercase(password) and digit(password) and special_char(password):
            return password


choice = input("Press 1 to enter a manual password or 2 to generate a random password: ")

if choice == '1':
    password = input("Enter a password: ")
    strength_result = check_password_strength(password)
    while "Weak" in strength_result:
        print("Password is weak. Please enter a stronger password.")
        password = input("Enter a password: ")
        strength_result = check_password_strength(password)
elif choice == '2':
    password = generate_random_password()
    print("Generated random password:", password)
else:
    print("Invalid choice.")
    exit()

strength_result = check_password_strength(password)
print(strength_result)
