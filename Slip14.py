# SLIP 14 – CYBER SECURITY

# Q1) Explain Man-In-The-Middle (MITM) attacks and Packet Sniffing along with their preventive measures. [10 Marks]

# 1. Man-In-The-Middle (MITM) Attack:
# A MITM attack occurs when an attacker secretly intercepts or alters communication between two parties without their knowledge.
# Example: An attacker intercepts communication between a user and a website over an insecure network.

# Preventive Measures:
# 1. Use HTTPS websites and secure connections.
# 2. Avoid connecting to unknown or unsecured Wi-Fi networks.
# 3. Use a trusted VPN when appropriate.
# 4. Verify website certificates and keep devices updated.

# 2. Packet Sniffing:
# Packet sniffing is the process of capturing and examining data packets travelling across a network.
# It can be used by network administrators for troubleshooting, but unauthorized sniffing may expose sensitive information.
# Example: An attacker captures unencrypted network traffic to look for sensitive information.

# Preventive Measures:
# 1. Use encryption protocols such as HTTPS and TLS.
# 2. Secure Wi-Fi networks with strong security settings.
# 3. Avoid sending sensitive information over untrusted networks.
# 4. Monitor network activity and restrict unauthorized access.

# Conclusion:
# MITM attacks intercept communication, while packet sniffing captures network packets. Encryption, secure connections, and network monitoring help protect against these threats.


# Q2) Write a Python program to simulate a SHA-256 hash generator that accepts user input text and computes its corresponding 256-bit hash value. [20 Marks]

import hashlib

text = input("Enter text: ")

hash_value = hashlib.sha256(text.encode()).hexdigest()

print("SHA-256 Hash:", hash_value)

# Output:
# Enter text: Hello
# SHA-256 Hash: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969

# Working:
# 1. Imports the built-in hashlib module.
# 2. Accepts text from the user.
# 3. Uses encode() to convert the text into bytes.
# 4. Uses hashlib.sha256() to calculate the SHA-256 hash.
# 5. Uses hexdigest() to display the hash as hexadecimal characters.
# 6. Displays the resulting 256-bit hash, represented by 64 hexadecimal characters.

# OR

# Q2) Write a program to display ASCII values of characters before encryption. [20 Marks]

text = input("Enter a message: ")

print("Characters and their ASCII values:")

for ch in text:
    print(ch, "=", ord(ch))

# Output:
# Enter a message: Hello
# Characters and their ASCII values:
# H = 72
# e = 101
# l = 108
# l = 108
# o = 111

# Working:
# 1. Accepts a message from the user.
# 2. Uses a for loop to process each character in the message.
# 3. Uses ord() to obtain the ASCII value of each character.
# 4. Displays each character and its corresponding numeric value.
# 5. These values can be used as a starting point for character-based encryption techniques.

# Requirements:
# Python 3 is required.
# Main program: No external libraries are required; hashlib is built into Python.
# OR program: No external libraries or files are required.
# Both programs can run independently in VS Code or Jupyter Notebook.

# VIVA QUESTIONS AND ANSWERS - SLIP 14

# Q1. What is a Man-In-The-Middle (MITM) attack?
# Ans: It is an attack in which someone secretly intercepts or alters communication between two parties.

# Q2. What is packet sniffing?
# Ans: It is the process of capturing and examining data packets travelling across a network.

# Q3. How can we prevent MITM attacks?
# Ans: Use HTTPS, secure Wi-Fi, trusted VPNs, and verify website certificates.

# Q4. What is SHA-256?
# Ans: SHA-256 is a cryptographic hash function that produces a 256-bit hash value.

# Q5. What is the purpose of ord() in Python?
# Ans: It returns the numeric Unicode value of a character. For ASCII characters, this is the ASCII value.