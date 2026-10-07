# Secure-Password-Generator
🔐 Secure Password Generator

A simple Python program that generates a secure 16-character random password using letters, numbers, and special characters.

I created this project to practice Python basics and learn how the "secrets" module can be used to generate more secure random values.

✨ Features

- Generates a 16-character password
- Includes uppercase and lowercase letters
- Includes numbers
- Includes special characters
- Uses Python's "secrets" module for secure random selection
- Simple and easy-to-understand code

🛠️ Technologies Used

- Python 3
- "secrets" module
- "string" module

🔎 How It Works

First, the program creates a collection of characters that can be used in the password:

characters = string.ascii_letters + string.digits + string.punctuation

The password length is set to 16 characters:

length = 16

Then, "secrets.choice()" randomly selects a character from the available characters for each position in the password:

password = "".join(secrets.choice(characters) for _ in range(length))

The generated password is then displayed in the terminal.

▶️ How to Run

1. Install Python

Make sure Python 3 is installed on your computer.

2. Clone this repository

git clone https://github.com/AryanSharma1105/secure-password-generator.git

3. Run the program

python password_generator.py

💻 Example Output

Your Secure Password is: K7@pQ!2x#Lm9$Rt&

The password will be different each time the program runs.

📚 What I Learned

While building this project, I learned and practiced:

- Importing Python modules
- Using the "secrets" module
- Using the "string" module
- Using "secrets.choice()"
- Working with strings
- Using "join()"
- Using a "for" loop with "range()"
- Generating secure random passwords

🔐 Why "secrets"?

Python's "secrets" module is designed for generating random values that are suitable for security-related applications, such as passwords and tokens.

This makes it a better choice for password generation than the basic "random" module.

🚀 Future Improvements

I may improve this project in the future by adding:

- Custom password length
- Options to include/exclude special characters
- A simple user interface
- Password strength checking

👨‍💻 About This Project

This is a beginner-friendly Python project created to practice programming fundamentals and understand secure password generation.

Built with Python 🐍

Author:-
