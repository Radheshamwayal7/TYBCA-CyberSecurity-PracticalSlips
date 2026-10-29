# SLIP 22 – CYBER SECURITY

# Q1) List any three types of files that can be used as carriers in steganography. [10 Marks]

# Answer:
#
# Steganography is a technique of hiding secret information inside
# another file without making the message easily noticeable.
#
# Three types of files used as carriers in steganography are:
#
# 1. Image Files:
# Secret messages can be hidden inside image files such as PNG and JPEG.
#
# 2. Audio Files:
# Secret information can be hidden inside audio files such as WAV and MP3.
#
# 3. Video Files:
# Secret messages can be hidden inside video files such as MP4 and AVI.
#
# These carrier files help conceal the existence of secret information.


# Q2) Write a program to verify file integrity using MD5, SHA-1, and SHA-256 hash values. [20 Marks]

import hashlib

filename = input("Enter file name: ")

try:
    with open(filename, "rb") as file:
        data = file.read()

    md5_hash = hashlib.md5(data).hexdigest()
    sha1_hash = hashlib.sha1(data).hexdigest()
    sha256_hash = hashlib.sha256(data).hexdigest()

    print("MD5:", md5_hash)
    print("SHA-1:", sha1_hash)
    print("SHA-256:", sha256_hash)

except FileNotFoundError:
    print("File not found. Please check the file name.")

# Sample Output:
# Enter file name: sample.txt
# MD5: (32 hexadecimal characters)
# SHA-1: (40 hexadecimal characters)
# SHA-256: (64 hexadecimal characters)

# Working:
# 1. Import the hashlib module.
# 2. Accept the file name from the user.
# 3. Open the file in binary read mode.
# 4. Read the file contents.
# 5. Calculate MD5, SHA-1, and SHA-256 hash values.
# 6. Display all three hash values.
# 7. If the file is missing, display an error message.
#
# File integrity verification:
# Calculate the hash again after the file is received or modified.
# Compare it with the original hash. If the values differ, the file
# contents have changed.
# Note: MD5 and SHA-1 are outdated for security-sensitive verification;
# SHA-256 is preferred.


# OR


# Q2) Write a Python program to check password strength: Length ≥ 8 and password must contain digits and special characters. [20 Marks]

import string

password = input("Enter password: ")

has_digit = any(ch.isdigit() for ch in password)
has_special = any(ch in string.punctuation for ch in password)

if len(password) >= 8 and has_digit and has_special:
    print("Password is strong.")
else:
    print("Password is weak.")
    print("Password must have at least 8 characters, a digit, and a special character.")

# Sample Output:
# Enter password: Hello@123
# Password is strong.

# Working:
# 1. Accept a password from the user.
# 2. Check whether its length is at least 8 characters.
# 3. Check whether it contains at least one digit.
# 4. Check whether it contains at least one special character.
# 5. Display whether the password meets the given rules.

# Requirements:
# Python 3. No external libraries are required.
# Main Q2 requires an existing file, such as sample.txt, in the
# working directory or the correct file path.
# OR Q2 does not require any external file.
# Run the two Q2 programs separately.

# VIVA QUESTIONS AND ANSWERS - SLIP 22

# Q1. What is steganography?
# Ans: It hides secret information inside another file.

# Q2. Name three carrier files used in steganography.
# Ans: Image, audio, and video files.

# Q3. What is a hash value?
# Ans: It is a fixed-length value calculated from data using a hash function.

# Q4. Which Python module is used to calculate hash values?
# Ans: hashlib.

# Q5. What conditions does the password program check?
# Ans: At least 8 characters, one digit, and one special character.