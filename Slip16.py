# SLIP 16 – CYBER SECURITY

# Q1) Describe the different types of Distributed Denial of Service (DDoS) flooding attacks. [10 Marks]

# Answer:
# A Distributed Denial of Service (DDoS) attack occurs when multiple
# compromised computers send excessive traffic to a target server or network.
# This makes the service slow or unavailable to legitimate users.
#
# Types of DDoS Flooding Attacks:
#
# 1. SYN Flood:
# The attacker sends many TCP connection requests without completing
# the connections, consuming server resources.
#
# 2. UDP Flood:
# A large number of UDP packets are sent to the target, consuming
# bandwidth and processing resources.
#
# 3. ICMP Flood:
# The target receives a large number of ICMP packets, consuming
# network bandwidth and system resources.
#
# 4. HTTP Flood:
# A large number of HTTP requests are sent to a web server, making
# it difficult to respond to genuine users.
#
# 5. DNS Amplification:
# Attackers exploit DNS servers to send large responses toward a
# target, increasing the volume of traffic reaching it.
#
# Prevention:
# Use firewalls, traffic filtering, rate limiting, DDoS protection
# services, and continuous network monitoring.


# Q2) Write a program using both ord() and chr() functions for Caesar Cipher. [20 Marks]

def caesar_cipher():
    text = input("Enter a message: ")
    shift = int(input("Enter shift value: "))
    result = ""

    for ch in text:
        if ch.isalpha() and ch.isascii():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch

    print("Encrypted message:", result)

caesar_cipher()

# Sample Output:
# Enter a message: Hello
# Enter shift value: 2
# Encrypted message: Jgnnq

# Working:
# 1. Accepts a message and shift value from the user.
# 2. Uses ord() to get the numeric value of each English alphabet.
# 3. Shifts each letter by the given number, wrapping around after Z or z.
# 4. Uses chr() to convert the shifted value back into a character.
# 5. Keeps spaces, numbers, symbols, and non-English characters unchanged.
# 6. Displays the encrypted message.


# OR


# Q2) Write a program to implement the RSA algorithm. Generate public and
# private keys, encrypt a message, and decrypt it. [20 Marks]

def rsa_algorithm():
    p = 3
    q = 11

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 7
    d = pow(e, -1, phi)

    message = int(input("Enter a number to encrypt (0 to 32): "))

    if message < 0 or message >= n:
        print("Enter a number between 0 and 32.")
    else:
        public_key = (e, n)
        private_key = (d, n)

        encrypted = pow(message, e, n)
        decrypted = pow(encrypted, d, n)

        print("Public key:", public_key)
        print("Private key:", private_key)
        print("Encrypted message:", encrypted)
        print("Decrypted message:", decrypted)

rsa_algorithm()

# Sample Output:
# Enter a number to encrypt (0 to 32): 5
# Public key: (7, 33)
# Private key: (3, 33)
# Encrypted message: 14
# Decrypted message: 5

# Working:
# 1. Select two prime numbers, p and q.
# 2. Calculate n = p * q and phi = (p - 1) * (q - 1).
# 3. Select e = 7 and calculate the private exponent d.
# 4. Generate the public key (e, n) and private key (d, n).
# 5. Encrypt the message using pow(message, e, n).
# 6. Decrypt the ciphertext using pow(encrypted, d, n).
# 7. Display both keys, the encrypted message, and the decrypted message.

# Requirements:
# Python 3.8 or later.
# No external libraries are required.
# Run the Caesar Cipher and RSA programs separately.
# The RSA example uses small numbers for educational purposes only.
# Real RSA requires large keys and a secure, standard implementation.

# VIVA QUESTIONS AND ANSWERS - SLIP 16

# Q1. What is a DDoS attack?
# Ans: It is an attack in which multiple devices send excessive traffic to a target.

# Q2. What are ord() and chr() in Python?
# Ans: ord() returns a character's numeric Unicode value, and chr() converts a number into a character.

# Q3. What is a Caesar Cipher?
# Ans: It is an encryption technique that shifts letters by a fixed number of positions.

# Q4. What is RSA?
# Ans: RSA is a public-key cryptographic algorithm used for encryption and digital signatures.

# Q5. What is the difference between public and private keys in RSA?
# Ans: The public key can be shared, while the private key must be kept secret.