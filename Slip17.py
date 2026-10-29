# SLIP 17 – CYBER SECURITY

# Q1) Write short notes on network security threats, including Man-In-The-Middle (MITM) and Packet Sniffing attacks. [10 Marks]

# Answer:
#
# Network security threats are activities that can damage a network,
# steal information, or gain unauthorized access to systems.
#
# 1. Man-In-The-Middle (MITM) Attack:
# A MITM attack occurs when an attacker secretly intercepts communication
# between two parties. The attacker may read or modify the information
# exchanged between them.
#
# Example:
# An attacker on an insecure public Wi-Fi network intercepts communication
# between a user and a website.
#
# Prevention:
# Use HTTPS, avoid unsecured public Wi-Fi for sensitive activities,
# use a VPN when appropriate, and verify website certificates.
#
# 2. Packet Sniffing:
# Packet sniffing is the process of capturing and examining data packets
# traveling through a network. Network administrators use it for
# troubleshooting, but attackers may misuse it to obtain sensitive data.
#
# Example:
# An attacker captures unencrypted network traffic to look for passwords.
#
# Prevention:
# Use encrypted protocols such as HTTPS and SSH, secure Wi-Fi networks,
# and monitor network traffic for suspicious activity.
#
# Other network threats include malware, phishing, password attacks,
# and Denial of Service (DoS) attacks.


# Q2) Write a Python program to simulate packet sniffing and alert for sensitive keywords like password and PIN. [20 Marks]

packets = [
    "User opened the home page",
    "Login request contains password field",
    "Payment request completed",
    "Message contains PIN information"
]

keywords = ["password", "pin"]

for packet in packets:
    print("Packet:", packet)

    for keyword in keywords:
        if keyword in packet.lower():
            print("ALERT: Sensitive keyword detected:", keyword)
            break

# Sample Output:
# Packet: User opened the home page
# Packet: Login request contains password field
# ALERT: Sensitive keyword detected: password
# Packet: Payment request completed
# Packet: Message contains PIN information
# ALERT: Sensitive keyword detected: pin

# Working:
# 1. Create a list of sample network packet messages.
# 2. Define sensitive keywords such as password and PIN.
# 3. Read each simulated packet from the list.
# 4. Convert the packet text to lowercase for comparison.
# 5. Search for sensitive keywords in each packet.
# 6. Display an alert when a keyword is detected.
# Note: This is a simulation; it does not capture real network packets.


# OR


# Q2) Write a Python program to implement Caesar Cipher for both encryption and decryption of a given text. [20 Marks]

def caesar_cipher(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch

    return result

message = input("Enter a message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_cipher(message, shift)
decrypted = caesar_cipher(encrypted, -shift)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)

# Sample Output:
# Enter a message: Hello
# Enter shift value: 3
# Encrypted message: Khoor
# Decrypted message: Hello

# Working:
# 1. Accept a message and shift value from the user.
# 2. Use ord() to convert each alphabet into a numeric value.
# 3. Shift each alphabet to create the encrypted message.
# 4. Use chr() to convert the shifted value back into a character.
# 5. Decrypt by applying the negative shift.
# 6. Display the encrypted and decrypted messages.

# Requirements:
# Python 3. No external libraries or files are required.
# Run the main program or the OR program separately.

# VIVA QUESTIONS AND ANSWERS - SLIP 17

# Q1. What is a network security threat?
# Ans: It is a threat that can damage a network or steal information.

# Q2. What is a MITM attack?
# Ans: An attacker secretly intercepts communication between two parties.

# Q3. What is packet sniffing?
# Ans: It is the process of capturing and examining network packets.

# Q4. What is the purpose of the packet sniffing simulation?
# Ans: It checks sample packet messages for sensitive keywords like password and PIN.

# Q5. What is a Caesar Cipher?
# Ans: It is an encryption technique that shifts letters by a fixed number of positions.