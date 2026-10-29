# SLIP 18 – CYBER SECURITY

# Q1) Define Steganography and distinguish it clearly from Cryptography. [10 Marks]

# Answer:
#
# Steganography:
# Steganography is a technique of hiding secret information inside
# another file, such as an image, audio, or video file, so that
# the existence of the message is concealed.
#
# Cryptography:
# Cryptography is a technique of converting readable information
# into an unreadable form to protect it from unauthorized access.
#
# Differences:
#
# 1. Steganography hides the existence of a message, whereas
#    cryptography hides the meaning of a message.
#
# 2. Steganography embeds secret data inside another file, whereas
#    cryptography transforms the original data using an algorithm.
#
# 3. Steganography may use images, audio, or video as carriers,
#    whereas cryptography uses encryption algorithms and keys.
#
# 4. Steganography may be detected by analyzing the carrier file,
#    whereas encrypted data may be recognized as ciphertext.
#
# 5. Both techniques help protect information and can be used
#    together for stronger security.
#
# Example:
# Hiding a secret message inside an image is steganography.
# Converting HELLO into encrypted text using a key is cryptography.


# Q2) Write a Python program that accepts a sentence from the user and encrypts it using Caesar Cipher. [20 Marks]

message = input("Enter a sentence: ")
shift = 3
encrypted = ""

for ch in message:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        encrypted += chr((ord(ch) - base + shift) % 26 + base)
    else:
        encrypted += ch

print("Encrypted message:", encrypted)

# Sample Output:
# Enter a sentence: Hello World
# Encrypted message: Khoor Zruog

# Working:
# 1. Accept a sentence from the user.
# 2. Set the shift value to 3.
# 3. Use ord() to get the numeric value of each alphabet.
# 4. Shift each alphabet forward by 3 positions.
# 5. Use chr() to convert the shifted value back to a character.
# 6. Keep spaces, digits, and punctuation unchanged.
# 7. Display the encrypted sentence.


# OR


# Q2) Write a Python program to implement AES encryption in ECB mode using the pycryptodome library to pad and encrypt a 16-byte message. [20 Marks]

# Install the library before running:
# python -m pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'0123456789abcdef'
message = b'Hello World 1234'

cipher = AES.new(key, AES.MODE_ECB)
padded_message = pad(message, AES.block_size)
encrypted = cipher.encrypt(padded_message)

print("Original message:", message.decode())
print("Padded message length:", len(padded_message))
print("Encrypted message:", encrypted.hex())

# Sample Output:
# Original message: Hello World 1234
# Padded message length: 32
# Encrypted message: (32-byte ciphertext displayed as hexadecimal)

# Working:
# 1. Import AES and the padding function from PyCryptodome.
# 2. Define a 16-byte AES key and a 16-byte message.
# 3. Create an AES cipher in ECB mode.
# 4. Apply PKCS#7 padding to the message.
# 5. Because the original message is already 16 bytes, padding adds
#    another full 16-byte block, making the total length 32 bytes.
# 6. Encrypt the padded message using AES.
# 7. Display the original message, padded length, and ciphertext.

# Requirements:
# Python 3.
# Main program: no external libraries required.
# OR program: install PyCryptodome using the command above.
# Run each Q2 program separately.
# Note: ECB mode is used here for the practical demonstration;
# it is not recommended for protecting real sensitive data.

# VIVA QUESTIONS AND ANSWERS - SLIP 18

# Q1. What is steganography?
# Ans: It hides the existence of secret information inside another file.

# Q2. What is the difference between steganography and cryptography?
# Ans: Steganography hides a message, while cryptography hides its meaning.

# Q3. What is a Caesar Cipher?
# Ans: It encrypts text by shifting letters by a fixed number of positions.

# Q4. What is AES?
# Ans: AES is a symmetric encryption algorithm that uses the same secret key for encryption and decryption.

# Q5. Why is padding required in this AES program?
# Ans: AES operates on 16-byte blocks, and PKCS#7 padding adds a full block when the message is already 16 bytes long.