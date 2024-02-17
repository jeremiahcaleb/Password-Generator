import random
import string
import os


def random_integer(min_val, max_val):
    if min_val > max_val:
        raise ValueError("Invalid range in random_integer function.")
    return random.randint(min_val, max_val)


def shuffle_string(input_string):
    string_list = list(input_string)
    random.shuffle(string_list)
    return "".join(string_list)


def generate_password(
    length,
    include_lowercase,
    include_uppercase,
    include_digits,
    include_special_chars,
    custom_chars,
    prefix,
    suffix,
    avoid_sequential,
):
    password = ""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+{}[]<>?"
    available_chars = ""

    if include_lowercase:
        available_chars += lowercase
    if include_uppercase:
        available_chars += uppercase
    if include_digits:
        available_chars += digits
    if include_special_chars:
        available_chars += special_chars
    available_chars += custom_chars

    if not available_chars:
        raise ValueError("No character types selected for password generation.")

    while len(password) < length:
        c = available_chars[random_integer(0, len(available_chars) - 1)]
        if avoid_sequential and password and c == password[-1]:
            continue
        password += c

    password = shuffle_string(password)

    password = prefix + password + suffix
    return password


def export(passwords):
    with open("passwords.txt", "w") as output_file:
        for password in passwords:
            output_file.write(password + "\n")
    print("Passwords exported to 'passwords.txt' in plain text format.")


def main():
    random.seed(os.urandom(1024))
    num_passwords = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter password length: "))
    include_lowercase = input("Include lowercase characters? (Y/N): ").lower() == "y"
    include_uppercase = input("Include uppercase characters? (Y/N): ").lower() == "y"
    include_digits = input("Include digits? (Y/N): ").lower() == "y"
    include_special_chars = input("Include special characters? (Y/N): ").lower() == "y"
    custom_chars = input("Enter custom characters (if any): ")
    prefix = input("Enter prefix (if any): ")
    suffix = input("Enter suffix (if any): ")
    avoid_sequential = input("Avoid sequential characters? (Y/N): ").lower() == "y"
    generated_passwords = []
    for i in range(num_passwords):
        password = generate_password(
            length,
            include_lowercase,
            include_uppercase,
            include_digits,
            include_special_chars,
            custom_chars,
            prefix,
            suffix,
            avoid_sequential,
        )
        print("Password {}: {}".format(i + 1, password))
        generated_passwords.append(password)
    export_choice = input("Do you want to export these passwords to a file? (Y/N): ")
    if export_choice.lower() == "y":
        export(generated_passwords)
    else:
        print("Passwords were not exported.")


main()
