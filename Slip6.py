# SLIP 6 – CYBER SECURITY

# Q1) Define Denial of Service (DoS) attack and explain its working principles along with SYN flood and HTTP flood attack types. [10 Marks]

# Definition:
# A Denial of Service (DoS) attack attempts to make a computer, server, or network unavailable to legitimate users by overwhelming its resources.

# Working Principle:
# 1. Excessive requests or traffic are sent to the target system.
# 2. The target consumes its bandwidth, memory, or processing resources.
# 3. The system becomes slow or unable to respond to genuine users.
# 4. Legitimate users may lose access to the service.

# Types of DoS Attacks:

# 1. SYN Flood:
# A SYN flood sends many TCP connection requests without completing the connections.
# This can consume server resources and prevent legitimate connections.

# 2. HTTP Flood:
# An HTTP flood sends excessive HTTP requests to a web server.
# Processing these requests can overload the server and make a website unavailable.

# Prevention:
# Use firewalls, traffic filtering, rate limiting, monitoring, and DDoS protection services.

# Conclusion:
# DoS attacks affect service availability by exhausting system resources. Proper security measures help reduce their impact.


# Q2) Write a Python program using Scapy to detect a possible DoS attack by counting packets received from each IP address and generating an alert when traffic exceeds a threshold. [20 Marks]

# Install library in terminal:
# python -m pip install scapy

from scapy.all import sniff, IP
from scapy.error import Scapy_Exception
from collections import Counter

packet_count = Counter()
THRESHOLD = 10

def check_packet(packet):
    if IP in packet:
        ip = packet[IP].src
        packet_count[ip] += 1

        print("IP:", ip, "Packets:", packet_count[ip])

        if packet_count[ip] == THRESHOLD + 1:
            print("ALERT: Possible DoS traffic from", ip)

print("Monitoring network traffic for 30 seconds...")

try:
    sniff(
        filter="ip",
        prn=check_packet,
        store=False,
        timeout=30
    )
    print("Monitoring completed.")

except (Scapy_Exception, OSError, PermissionError) as error:
    print("Packet capture error:", error)
    print("Check permissions, network interface, and Npcap installation.")

# Output (illustrative):
# Monitoring network traffic for 30 seconds...
# IP: 192.168.1.5 Packets: 1
# IP: 192.168.1.5 Packets: 2
# ...
# IP: 192.168.1.5 Packets: 11
# ALERT: Possible DoS traffic from 192.168.1.5
# Monitoring completed.

# Working:
# 1. Imports Scapy functions and Counter for packet capture and counting.
# 2. Sets the threshold to 10 packets for each source IP.
# 3. Captures IP packets for 30 seconds and passes them to check_packet().
# 4. Extracts each source IP and increments its packet count.
# 5. Displays an alert when an IP exceeds 10 packets.
# 6. Stops automatically after 30 seconds and handles common capture errors.

# Requirements:
# Python 3 is required.
# Install Scapy using: python -m pip install scapy
# Windows may require Npcap and administrator permissions.
# If necessary, select the correct network interface.
# No external files are required.
# This is a basic traffic-monitoring demonstration, not definitive proof of a DoS attack.


# OR

# Q2) Write a Python program to implement Caesar Cipher for both encryption and decryption of a given text. [20 Marks]

text = input("Enter a message: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for ch in text:
    if ch.isupper():
        encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    elif ch.islower():
        encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    else:
        encrypted += ch

print("Encrypted message:", encrypted)

decrypted = ""

for ch in encrypted:
    if ch.isupper():
        decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
    elif ch.islower():
        decrypted += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
    else:
        decrypted += ch

print("Decrypted message:", decrypted)

# Output:
# Enter a message: Hello
# Enter shift value: 3
# Encrypted message: Khoor
# Decrypted message: Hello

# Working:
# 1. Accepts a message and shift value.
# 2. Shifts each alphabet forward to encrypt the message.
# 3. Uses ord() and chr() to convert between characters and numeric values.
# 4. Uses modulo 26 to wrap around the alphabet.
# 5. Shifts the encrypted message backward to decrypt it.
# 6. Displays the encrypted and decrypted messages.

# Requirements:
# Python 3 is required.
# No external libraries or files are required for the Caesar Cipher program.

# VIVA QUESTIONS AND ANSWERS - SLIP 6

# Q1. What is a DoS attack?
# Ans: It attempts to make a service unavailable to legitimate users.

# Q2. What is a SYN flood attack?
# Ans: It sends many TCP connection requests without completing the connections.

# Q3. What is Scapy?
# Ans: Scapy is a Python library used to capture, send, and analyze network packets.

# Q4. How does the program detect possible DoS traffic?
# Ans: It counts packets from each source IP and generates an alert when the count exceeds 10.

# Q5. What is a Caesar Cipher?
# Ans: It is an encryption technique that shifts letters by a fixed number of positions.