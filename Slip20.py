# SLIP 20 – CYBER SECURITY

# Q1) Describe the different types of Distributed Denial of Service (DDoS) flooding attacks. [10 Marks]

# Answer:
#
# A Distributed Denial of Service (DDoS) attack occurs when multiple
# compromised computers send excessive traffic to a target server or
# network, making the service unavailable to genuine users.
#
# Types of DDoS flooding attacks:
#
# 1. SYN Flood:
# The attacker sends many TCP connection requests without completing
# the connections, consuming server resources.
#
# 2. UDP Flood:
# A large number of UDP packets are sent to the target, consuming
# network bandwidth and system resources.
#
# 3. ICMP Flood:
# The target receives a large number of ICMP packets, which can
# overload the network or system.
#
# 4. HTTP Flood:
# The attacker sends a large number of HTTP requests to a web server,
# making it difficult to respond to legitimate users.
#
# 5. DNS Amplification:
# Attackers misuse DNS servers to send large responses toward a target,
# increasing the amount of traffic reaching it.
#
# Prevention:
# Use firewalls, traffic filtering, rate limiting, DDoS protection
# services, and network traffic monitoring.


# Q2) Write a Python program to detect spam emails using predefined keywords. [20 Marks]

email = input("Enter email message: ").lower()

spam_keywords = ["win", "prize", "free", "offer", "lottery"]

found = False

for word in spam_keywords:
    if word in email:
        print("Spam email detected!")
        print("Keyword found:", word)
        found = True
        break

if not found:
    print("Email is not detected as spam.")

# Sample Output:
# Enter email message: You have won a free prize
# Spam email detected!
# Keyword found: prize

# Working:
# 1. Accept an email message from the user.
# 2. Convert the message to lowercase.
# 3. Define a list of common spam-related keywords.
# 4. Check whether any keyword appears in the message.
# 5. If a keyword is found, display a spam alert.
# 6. Otherwise, display that the email was not detected as spam.
# Note: This is a basic demonstration and may produce false results.


# OR


# Q2) Write a program to display ASCII values of characters before encryption. [20 Marks]

text = input("Enter a message: ")

print("Characters and their ASCII values:")

for ch in text:
    print(ch, ":", ord(ch))

# Sample Output:
# Enter a message: CAT
# Characters and their ASCII values:
# C : 67
# A : 65
# T : 84

# Working:
# 1. Accept a message from the user.
# 2. Read each character in the message.
# 3. Use the ord() function to find its numeric code.
# 4. Display each character and its ASCII value.

# Requirements:
# Python 3. No external libraries or files are required.
# Run the main Q2 program or the OR program separately.

# VIVA QUESTIONS AND ANSWERS - SLIP 20

# Q1. What is a DDoS attack?
# Ans: It uses multiple devices to send excessive traffic to a target.

# Q2. What is a spam email?
# Ans: It is an unwanted or unsolicited email, often sent in bulk.

# Q3. How does the spam detection program work?
# Ans: It checks the email message for predefined spam keywords.

# Q4. What is the purpose of ord()?
# Ans: It returns the numeric Unicode code point of a character.

# Q5. What is ASCII?
# Ans: ASCII is a character-encoding standard for representing characters using numeric codes.