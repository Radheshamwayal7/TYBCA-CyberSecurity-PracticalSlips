# SLIP 13 – CYBER SECURITY

# Q1) Write a program to encrypt a message using Caesar Cipher. [10 Marks]

# Definition:
# Caesar Cipher is a substitution encryption technique in which each alphabet is shifted by a fixed number of positions.
# Example: With a shift of 3, A becomes D, B becomes E, and Z becomes C.

text = input("Enter a message: ")
shift = 3
encrypted = ""

for ch in text:
    if ch.isupper():
        encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    elif ch.islower():
        encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    else:
        encrypted += ch

print("Encrypted message:", encrypted)

# Output:
# Enter a message: Hello World
# Encrypted message: Khoor Zruog

# Working:
# 1. Accepts a message from the user and sets the shift value to 3.
# 2. Checks each character to determine whether it is uppercase or lowercase.
# 3. Uses ord() to convert a character into its numeric value and shifts it forward by 3.
# 4. Uses chr() to convert the shifted value back into a character.
# 5. Uses modulo 26 to wrap around the alphabet and preserves spaces and punctuation.
# 6. Displays the encrypted message.


# Q2) Implement a Python program to detect a possible DoS/DDoS attack by monitoring network traffic. [20 Marks]

# Install library in terminal:
# python -m pip install scapy

from scapy.all import sniff, IP
from collections import Counter

packet_count = Counter()
THRESHOLD = 10

def check_packet(packet):
    if IP in packet:
        ip = packet[IP].src
        packet_count[ip] += 1

        print("IP:", ip, "Packets:", packet_count[ip])

        if packet_count[ip] == THRESHOLD + 1:
            print("ALERT: Possible DoS/DDoS traffic from", ip)

print("Monitoring network traffic for 30 seconds...")

sniff(
    filter="ip",
    prn=check_packet,
    store=False,
    timeout=30
)

print("Monitoring completed.")

# Output (illustrative):
# Monitoring network traffic for 30 seconds...
# IP: 192.168.1.5 Packets: 1
# IP: 192.168.1.5 Packets: 2
# ...
# IP: 192.168.1.5 Packets: 11
# ALERT: Possible DoS/DDoS traffic from 192.168.1.5
# Monitoring completed.

# Working:
# 1. Imports Scapy to capture network packets and Counter to count packets by source IP.
# 2. Sets the threshold to 10 packets per IP address.
# 3. Captures IP traffic for 30 seconds and passes each packet to check_packet().
# 4. Extracts the source IP address and increases its packet count.
# 5. Displays an alert when an IP address exceeds 10 packets.
# 6. Stops after 30 seconds and displays a completion message.

# OR

# Q2) Write a Python program to implement AES encryption and decryption using a custom secret key. [20 Marks]

# Install library in terminal:
# python -m pip install pycryptodome

from Crypto.Cipher import AES

key_text = input("Enter a 16-character secret key: ")

if len(key_text.encode("utf-8")) != 16:
    print("Error: Key must be exactly 16 bytes.")
else:
    key = key_text.encode("utf-8")
    message = input("Enter a message: ")

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode("utf-8"))

    print("Encrypted message:", ciphertext.hex())

    decipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
    decrypted = decipher.decrypt_and_verify(ciphertext, tag)

    print("Decrypted message:", decrypted.decode("utf-8"))

# Output (illustrative):
# Enter a 16-character secret key: 1234567890123456
# Enter a message: Hello
# Encrypted message: <generated ciphertext>
# Decrypted message: Hello

# Working:
# 1. Accepts a custom secret key and checks that it is exactly 16 bytes long.
# 2. Accepts a message and converts it into bytes.
# 3. Creates an AES cipher using EAX mode and encrypts the message.
# 4. Generates a nonce and authentication tag to support secure decryption and verification.
# 5. Creates a decryption object using the same key and nonce.
# 6. Verifies the authentication tag, decrypts the ciphertext, and displays the original message.

# Requirements:
# Python 3 is required.
# Q1: No external libraries or files are required.
# Main Q2: Install Scapy using python -m pip install scapy.
# Network monitoring may require administrator permissions and Npcap on Windows.
# OR Q2: Install PyCryptodome using python -m pip install pycryptodome.
# No external files are required.
# Run each program separately.
# Note: The traffic threshold is only a basic indicator; it cannot confirm a DoS/DDoS attack by itself.

# VIVA QUESTIONS AND ANSWERS - SLIP 13

# Q1. What is a Caesar Cipher?
# Ans: It is an encryption technique that shifts each alphabet by a fixed number of positions.

# Q2. What are ord() and chr() in Python?
# Ans: ord() converts a character into its numeric Unicode value, and chr() converts a numeric value into a character.

# Q3. What is a DoS attack?
# Ans: A Denial-of-Service attack attempts to make a system or service unavailable to users.

# Q4. What is Scapy?
# Ans: Scapy is a Python library used to capture, send, and analyze network packets.

# Q5. What is AES?
# Ans: AES stands for Advanced Encryption Standard. It is a symmetric encryption algorithm that uses the same secret key for encryption and decryption.