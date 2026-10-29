# SLIP 8 – CYBER SECURITY

# Q1) Define Steganography and distinguish it clearly from Cryptography. [10 Marks]

# Definition:
# Steganography is a technique of hiding secret information inside an ordinary file, such as an image, audio file, or video, so that the existence of the information is concealed.
# Example: Hiding a secret text message inside an image.

# Cryptography:
# Cryptography is the technique of converting readable information (plaintext) into an unreadable form (ciphertext) to protect it from unauthorized access.
# Example: Encrypting a message using Caesar Cipher.

# Differences:
# 1. Steganography hides the existence of a message, whereas cryptography hides the meaning of a message.
# 2. Steganography uses a carrier file, such as an image or audio file, whereas cryptography uses encryption algorithms and keys.
# 3. Steganography may be detected by analyzing the carrier file, whereas encrypted data may be recognized as ciphertext.
# 4. Steganography focuses on hiding information, whereas cryptography focuses on protecting information.

# Conclusion:
# Both steganography and cryptography protect information. Steganography hides the message itself, while cryptography makes the message unreadable without the appropriate key.


# Q2) Write a Python program that accepts a sentence from the user and encrypts it using Caesar Cipher. [20 Marks]

text = input("Enter a sentence: ")
shift = 3

encrypted = ""

for ch in text:
    if ch.isupper():
        encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    elif ch.islower():
        encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    else:
        encrypted += ch

print("Encrypted sentence:", encrypted)

# Output:
# Enter a sentence: Hello World
# Encrypted sentence: Khoor Zruog

# Working:
# 1. Accepts a sentence from the user and sets the shift value to 3.
# 2. Checks each character to determine whether it is uppercase or lowercase.
# 3. Uses ord() to obtain the character's numeric value and shifts it forward by three positions.
# 4. Uses chr() to convert the shifted value back into a character.
# 5. Uses modulo 26 to wrap around the alphabet when necessary.
# 6. Keeps spaces, numbers, and punctuation unchanged and displays the encrypted sentence.

# OR

# Q2) Write a Python program to implement a dictionary attack using a list of common passwords to check whether a target password exists in the list. [20 Marks]

common_passwords = [
    "123456",
    "password",
    "admin123",
    "welcome",
    "student123"
]

target_password = input("Enter a test password: ")

if target_password in common_passwords:
    print("Password found in the dictionary!")
else:
    print("Password not found in the dictionary.")

# Output:
# Enter a test password: admin123
# Password found in the dictionary!

# Working:
# 1. Creates a list containing commonly used passwords.
# 2. Accepts a test password from the user.
# 3. Uses the in operator to check whether the entered password exists in the list.
# 4. If the password is found, displays a success message; otherwise, displays that it was not found.
# 5. This is a basic demonstration using a local list, not an attempt to access an actual account.

# Requirements:
# Python 3 is required.
# No external libraries or additional files are required.
# Both programs can run independently in VS Code or Jupyter Notebook.

# VIVA QUESTIONS AND ANSWERS - SLIP 8

# Q1. What is steganography?
# Ans: It hides secret information inside another file.

# Q2. What is the difference between steganography and cryptography?
# Ans: Steganography hides the existence of a message, while cryptography hides its meaning.

# Q3. What is a Caesar Cipher?
# Ans: It encrypts text by shifting letters by a fixed number of positions.

# Q4. What is a dictionary attack?
# Ans: It checks passwords against a predefined list of common passwords.

# Q5. What is the purpose of the in operator in Python?
# Ans: It checks whether an item exists in a list or another collection.