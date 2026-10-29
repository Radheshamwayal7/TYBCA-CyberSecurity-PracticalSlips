# SLIP 2 – CYBER SECURITY

# Q1) Differentiate between virus, worm, and Trojan horse. [10 Marks]

# 1. Virus:
# A virus is a malicious program that attaches itself to a file or program and spreads when the infected file is executed.
# Example: A virus that infects files on a computer.

# 2. Worm:
# A worm is a malicious program that replicates itself and spreads across computers or networks without requiring a host file.
# Example: A worm that spreads automatically through a computer network.

# 3. Trojan Horse:
# A Trojan horse is a malicious program that appears to be legitimate software but performs harmful activities when executed.
# Example: A fake application that secretly steals data.

# Differences:
# Virus: Requires a host file or program to spread.
# Worm: Can spread independently across networks.
# Trojan Horse: Disguises itself as legitimate software and tricks users into running it.

# Conclusion:
# Viruses, worms, and Trojan horses are types of malware that threaten computer security in different ways.


# Q2) Write a Python program to detect spam emails using predefined keywords. [20 Marks]

spam_keywords = [
    "win money",
    "free prize",
    "claim now",
    "urgent",
    "lottery"
]

email = input("Enter email message: ").lower()

found = False

for keyword in spam_keywords:
    if keyword in email:
        found = True
        break

if found:
    print("Spam email detected!")
else:
    print("Email is not spam.")

# Output:
# Enter email message: Congratulations! You win money
# Spam email detected!

# Working:
# 1. Creates a list of predefined words and phrases commonly found in spam emails.
# 2. Accepts an email message and converts it to lowercase.
# 3. Checks whether any spam keyword is present in the message.
# 4. Displays a spam warning if a keyword is found; otherwise, it displays that the email is not spam.

# OR

# Corrected AES Program for Slip 2

# Q2) Write a Python program to encrypt user input text using AES encryption. [20 Marks]

# Install library in terminal:
# python -m pip install pycryptodome

from Crypto.Cipher import AES

key = b"1234567890123456"

message = input("Enter text to encrypt: ")

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(message.encode())

print("Encrypted text:", ciphertext.hex())
print("Nonce:", cipher.nonce.hex())
print("Authentication tag:", tag.hex())

# Output:
# Enter text to encrypt: Hello
# Encrypted text: <generated ciphertext>
# Nonce: <generated nonce>
# Authentication tag: <generated authentication tag>

# Working:
# 1. Imports the AES class from the PyCryptodome library.
# 2. Defines a 16-byte secret key for AES-128 encryption.
# 3. Accepts a message from the user and converts it into bytes.
# 4. Creates an AES cipher using EAX mode and generates a unique nonce.
# 5. Encrypts the message and generates an authentication tag.
# 6. Displays the ciphertext, nonce, and authentication tag in hexadecimal format.

# Requirements:
# Python 3 is required.
# Install PyCryptodome using:
# python -m pip install pycryptodome
# No external files are required.

# VIVA QUESTIONS AND ANSWERS - SLIP 2

# Q1. What is the difference between a virus, worm, and Trojan horse?
# Ans: A virus attaches to a file, a worm spreads independently, and a Trojan disguises itself as legitimate software.

# Q2. What is spam?
# Ans: Spam is unwanted or unsolicited electronic messages, often sent in bulk.

# Q3. How does the spam detection program work?
# Ans: It checks the email message for predefined spam keywords.

# Q4. What is AES?
# Ans: AES stands for Advanced Encryption Standard, a symmetric encryption algorithm.

# Q5. What is the purpose of the nonce in AES EAX mode?
# Ans: The nonce is a value used by the encryption mode to help ensure secure encryption; it must be unique for each encryption with the same key.