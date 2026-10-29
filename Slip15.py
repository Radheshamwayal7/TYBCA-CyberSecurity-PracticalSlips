# SLIP 15 – CYBER SECURITY

# Q1) Explain the concepts of Salami Attack, Data Diddling, Web Jacking, and Email Bombing as forms of cyber offenses. [10 Marks]

# 1. Salami Attack:
# A Salami Attack is a cyber offense in which an attacker makes very small changes or deductions from many transactions to gain an unauthorized benefit.
# Example: Deducting a tiny amount from many financial transactions without authorization.

# 2. Data Diddling:
# Data Diddling means changing data before, during, or after it is entered into a computer system without authorization.
# Example: Illegally changing marks in a student's database.

# 3. Web Jacking:
# Web Jacking is an attack in which an attacker takes unauthorized control of a website or redirects users to a fake website.
# Example: Redirecting visitors from a genuine website to a fraudulent website.

# 4. Email Bombing:
# Email Bombing is an attack in which a victim receives an extremely large number of unwanted emails, potentially disrupting email services.
# Example: Flooding an email inbox with repeated unwanted messages.

# Conclusion:
# These cyber offenses can cause financial loss, data manipulation, website disruption, and communication problems. Strong security controls and monitoring help prevent them.


# Q2) Write a Python program to simulate a Brute Force Attack that generates all 3-character combinations from a given set of characters to discover a target password. [20 Marks]

from itertools import product

characters = "abcdefghijklmnopqrstuvwxyz"
target_password = input("Enter a 3-character test password: ")

if len(target_password) != 3 or any(ch not in characters for ch in target_password):
    print("Enter exactly 3 lowercase English letters.")
else:
    found = False
    attempts = 0

    for combination in product(characters, repeat=3):
        guess = ''.join(combination)
        attempts += 1

        if guess == target_password:
            print("Password found:", guess)
            print("Attempts:", attempts)
            found = True
            break

    if not found:
        print("Password not found.")

# Output:
# Enter a 3-character test password: cat
# Password found: cat
# Attempts: 1372

# Working:
# 1. Imports product() from the built-in itertools module.
# 2. Defines a set of lowercase English letters and accepts a three-character test password.
# 3. Uses product() with repeat=3 to generate all possible three-letter combinations.
# 4. Joins each combination into a string and compares it with the target password.
# 5. Counts each attempt and stops when the correct password is found.
# 6. Displays the matching password and the number of attempts.

# OR

# Q2) Write a Python program to demonstrate IP tracking (simulation): Store fake IP addresses and print location mapping using a dictionary. [20 Marks]

ip_locations = {
    "192.168.1.1": "Pune",
    "192.168.1.2": "Mumbai",
    "192.168.1.3": "Nashik",
    "192.168.1.4": "Delhi"
}

ip = input("Enter an IP address: ")

if ip in ip_locations:
    print("Location:", ip_locations[ip])
else:
    print("IP address not found.")

# Output:
# Enter an IP address: 192.168.1.2
# Location: Mumbai

# Working:
# 1. Creates a dictionary containing fake IP addresses and their sample location mappings.
# 2. Accepts an IP address from the user.
# 3. Checks whether the entered address exists in the dictionary.
# 4. If the address exists, displays its mapped location.
# 5. Otherwise, displays "IP address not found."
# 6. This is a simulation and does not determine the actual location of an IP address.

# Requirements:
# Python 3 is required.
# No external libraries or additional files are required.
# Both programs can run independently in VS Code or Jupyter Notebook.
# Use only a dummy password for the brute-force demonstration.

# VIVA QUESTIONS AND ANSWERS - SLIP 15

# Q1. What is a brute-force attack?
# Ans: It tries different combinations to find the correct password.

# Q2. Which module generates combinations in Python?
# Ans: itertools.

# Q3. How many 3-character combinations are possible using 26 letters?
# Ans: 17,576.

# Q4. What is a dictionary in Python?
# Ans: It stores data in key-value pairs.

# Q5. Does the IP tracking program find the real location?
# Ans: No, it uses predefined sample IP-to-location mappings.