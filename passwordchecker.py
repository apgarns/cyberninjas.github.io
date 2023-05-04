import string
import math
from getpass import getpass

def password_strength(password):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    has_lower = any(char in lower for char in password)
    has_upper = any(char in upper for char in password)
    has_digits = any(char in digits for char in password)
    has_special = any(char in special for char in password)

    character_set = 0
    if has_lower:
        character_set += len(lower)
    if has_upper:
        character_set += len(upper)
    if has_digits:
        character_set += len(digits)
    if has_special:
        character_set += len(special)

    combinations = character_set ** len(password)
    return combinations

def cracking_time(combinations, attempts_per_second=10**9):
    seconds = combinations / attempts_per_second

    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    return years

def main():
    password = getpass("Enter your password: ")
    strength = password_strength(password)
    time_to_crack = cracking_time(strength)

    print(f"Your password has {strength} possible combinations.")
    print(f"It would take approximately {time_to_crack:.2f} years to crack your password with a brute-force attack.")

if __name__ == "__main__":
    main()
