# SLIP 4 – CYBER SECURITY

# Q1) Explain Brute Force Attacks with an example, detailing Simple, Dictionary, and Hybrid brute force types. [10 Marks]

# Definition:
# A brute force attack is a password-guessing technique in which an attacker tries different possible passwords until the correct one is found.

# 1. Simple Brute Force Attack:
# It tries different combinations of characters, numbers, and symbols until a matching password is found.
# Example: Trying passwords such as abc, abd, and abe.

# 2. Dictionary Attack:
# It tries passwords from a predefined list of commonly used passwords.
# Example: Checking passwords such as password123, admin123, and welcome.

# 3. Hybrid Brute Force Attack:
# It combines dictionary words with additional characters, numbers, or symbols to generate password guesses.
# Example: Trying password123 or welcome2026.

# Prevention:
# Use long and unique passwords, enable multi-factor authentication, and apply account lockout or rate-limiting mechanisms.

# Conclusion:
# Brute force attacks attempt to discover passwords through repeated guesses. Strong passwords and additional security measures help protect accounts.


# Q2) Write a Python program to demonstrate IP tracking simulation by storing fake IP addresses and printing location mapping using a dictionary. [20 Marks]

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
# 1. Creates a dictionary containing fake IP addresses as keys and sample locations as values.
# 2. Accepts an IP address from the user.
# 3. Checks whether the entered IP address exists in the dictionary.
# 4. If found, displays its mapped location; otherwise, displays an error message.
# 5. This is only a simulation and does not track real IP addresses or determine actual locations.

# OR

# Q2) Write a Python program to check password strength based on basic security rules. [20 Marks]

password = input("Enter a password: ")

if (len(password) >= 8
        and any(ch.isdigit() for ch in password)
        and any(not ch.isalnum() for ch in password)):
    print("Password is strong.")
else:
    print("Password is weak.")
    print("Use at least 8 characters, a digit, and a special character.")

# Output:
# Enter a password: Hello@123
# Password is strong.

# Working:
# 1. Accepts a password from the user.
# 2. The len() function checks whether the password has at least 8 characters.
# 3. The first any() function checks whether the password contains a digit.
# 4. The second any() function checks whether the password contains a special character.
# 5. If all three conditions are satisfied, the program displays that the password is strong.
# 6. Otherwise, it displays that the password is weak and shows the required rules.

# Requirements:
# Python 3 is required.
# No external libraries or additional files are required.
# Both programs can run independently in VS Code or Jupyter Notebook.

# VIVA QUESTIONS AND ANSWERS - SLIP 4

# Q1. What is a brute-force attack?
# Ans: It tries different password combinations to find the correct password.

# Q2. What is the difference between simple, dictionary, and hybrid attacks?
# Ans: Simple tries combinations, dictionary tries common passwords, and hybrid combines words with extra characters.

# Q3. What is a dictionary in Python?
# Ans: It stores data in key-value pairs.

# Q4. What is the purpose of the len() function?
# Ans: It returns the number of characters in a password.

# Q5. What does the any() function do?
# Ans: It returns True if at least one item satisfies the given condition.