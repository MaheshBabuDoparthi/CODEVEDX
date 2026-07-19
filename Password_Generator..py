import random
import string
from datetime import datetime


# ==========================
# PASSWORD GENERATOR
# ==========================

def generate_password(length, upper, lower, digits, symbols):

    password = []
    characters = ""

    if upper:
        password.append(random.choice(string.ascii_uppercase))
        characters += string.ascii_uppercase

    if lower:
        password.append(random.choice(string.ascii_lowercase))
        characters += string.ascii_lowercase

    if digits:
        password.append(random.choice(string.digits))
        characters += string.digits

    if symbols:
        password.append(random.choice(string.punctuation))
        characters += string.punctuation

    if characters == "":
        return None

    if length < len(password):
        return None

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)


# ==========================
# PASSWORD STRENGTH
# ==========================

def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score == 3:
        return "Medium"

    elif score == 4:
        return "Strong"

    else:
        return "Very Strong"


# ==========================
# PASSWORD SUGGESTIONS
# ==========================

def password_suggestions(password):

    print("\nSuggestions:")

    if len(password) < 8:
        print("- Use at least 8 characters.")

    if not any(c.isupper() for c in password):
        print("- Add uppercase letters.")

    if not any(c.islower() for c in password):
        print("- Add lowercase letters.")

    if not any(c.isdigit() for c in password):
        print("- Add numbers.")

    if not any(c in string.punctuation for c in password):
        print("- Add special characters.")


# ==========================
# SAVE PASSWORD
# ==========================

def save_password(password):

    strength = check_strength(password)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file = open("passwords.txt", "a")

    file.write(f"Date & Time : {current_time}\n")
    file.write(f"Password    : {password}\n")
    file.write(f"Strength    : {strength}\n")
    file.write("-" * 40 + "\n")

    file.close()
        # ==========================
# VIEW PASSWORD HISTORY
# ==========================

def view_history():

    try:
        file = open("passwords.txt", "r")
        data = file.read()

        if data.strip() == "":
            print("\nNo Password History Found!")

        else:
            print("\n========== PASSWORD HISTORY ==========")
            print(data)

        file.close()

    except FileNotFoundError:
        print("\nNo Password History Found!")


# ==========================
# CLEAR PASSWORD HISTORY
# ==========================

def clear_history():

    file = open("passwords.txt", "w")
    file.close()

    print("\nPassword History Cleared Successfully!")


# ==========================
# PASSWORD STATISTICS
# ==========================

def password_statistics():

    try:

        file = open("passwords.txt", "r")
        lines = file.readlines()
        file.close()

        total = 0
        weak = 0
        medium = 0
        strong = 0
        very_strong = 0

        for line in lines:

            if line.startswith("Strength"):

                total += 1

                if "Very Strong" in line:
                    very_strong += 1

                elif "Strong" in line:
                    strong += 1

                elif "Medium" in line:
                    medium += 1

                elif "Weak" in line:
                    weak += 1

        print("\n========== PASSWORD STATISTICS ==========")
        print("Total Passwords :", total)
        print("Weak            :", weak)
        print("Medium          :", medium)
        print("Strong          :", strong)
        print("Very Strong     :", very_strong)

    except FileNotFoundError:
        print("\nNo Password History Found!")
        # ==========================
# MAIN MENU
# ==========================

while True:

    print("\n========== PASSWORD GENERATOR ==========")
    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. View Password History")
    print("4. Clear Password History")
    print("5. Password Statistics")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        try:
            length = int(input("Enter Password Length: "))

            if length < 4:
                print("Password length must be at least 4.")
                continue

            upper = input("Include Uppercase (y/n): ").lower() == "y"
            lower = input("Include Lowercase (y/n): ").lower() == "y"
            digits = input("Include Numbers (y/n): ").lower() == "y"
            symbols = input("Include Special Characters (y/n): ").lower() == "y"

            if not (upper or lower or digits or symbols):
                print("Please select at least one character type.")
                continue

            password = generate_password(length, upper, lower, digits, symbols)

            if password is None:
                print("Unable to generate password.")
                continue

            print("\nGenerated Password :", password)

            strength = check_strength(password)
            print("Password Strength :", strength)

            if strength == "Weak":
                password_suggestions(password)

            save_password(password)

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":

        password = input("Enter Password: ")

        strength = check_strength(password)

        print("Password Strength :", strength)

        if strength == "Weak":
            password_suggestions(password)

    elif choice == "3":

        view_history()

    elif choice == "4":

        clear_history()

    elif choice == "5":

        password_statistics()

    elif choice == "6":

        print("\nThank you for using Password Generator!")
        break

    else:

        print("\nInvalid Choice! Please try again.")