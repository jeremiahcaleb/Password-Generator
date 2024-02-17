# Password Generator

This is a simple Python script that generates random passwords based on user preferences.

## Features

- Generates random passwords with customizable options:
  - Length of the password
  - Inclusion of lowercase, uppercase, digits, and special characters
  - Custom characters
  - Prefix and suffix for the password
  - Option to avoid sequential characters
- Allows users to specify the number of passwords to generate.
- Provides an option to export generated passwords to a text file.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:

```bash
git clone https://github.com/jeremiahcaleb/Password-Generator.git
```

2. Navigate to the directory

3. Run the code from the command line:

   ```bash
   python password_generator.py
   ```
   
Follow the on-screen prompts to generate passwords with your desired configurations.

## Example Output

```
Enter the number of passwords to generate: 1
Enter password length: 12
Include lowercase characters? (Y/N): Y
Include uppercase characters? (Y/N): Y
Include digits? (Y/N): Y
Include special characters? (Y/N): Y
Enter custom characters (if any):
Enter prefix (if any):
Enter suffix (if any):
Avoid sequential characters? (Y/N): Y
Password 1: ktEk4AXH&uoy
Do you want to export these passwords to a file? (Y/N): Y
Passwords exported to 'passwords.txt' in plain text format.
```

## How It Works

The script follows these steps to generate passwords:

1. Prompts the user to input preferences for password generation, such as length, character types, prefix/suffix, and avoidance of sequential characters.
2. Generates random passwords based on the provided preferences using Python's built-in `random` module.
3. Provides an option to export the generated passwords to a text file named `passwords.txt` in the current directory.

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.
