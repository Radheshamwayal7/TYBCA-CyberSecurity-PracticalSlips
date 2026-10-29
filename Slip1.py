# SLIP 1 – CYBER SECURITY

# Q1) Explain the CIA triad (Confidentiality, Integrity, Availability) with suitable examples. [10 Marks]

# 1. Confidentiality:
# Confidentiality means protecting information from unauthorized access or disclosure.
# Example: A password protects a bank account from unauthorized access.

# 2. Integrity:
# Integrity means maintaining the accuracy and completeness of data and preventing unauthorized changes.
# Example: A bank ensures that account balances are changed only through authorized transactions.

# 3. Availability:
# Availability means ensuring that information and services are accessible to authorized users whenever required.
# Example: A hospital database should be available to doctors whenever they need patient records.

# Conclusion:
# The CIA triad protects information through Confidentiality, Integrity, and Availability.


# Q2) Write a Python program to simulate a phishing login page that collects username and password and stores them in a file. [20 Marks]

username = input("Enter username: ")
password = input("Enter password: ")

with open("login_log.txt", "a") as file:
    file.write("Username: " + username + "\n")
    file.write("Password: [REDACTED]\n")
    file.write("--------------------\n")

print("Login simulation completed.")
print("Record saved in login_log.txt")

# Output:
# Enter username: student
# Enter password: test123
# Login simulation completed.
# Record saved in login_log.txt

# Working:
# 1. Accepts the username and password from the user.
# 2. Opens login_log.txt in append mode and creates it if it does not exist.
# 3. Writes the username and a redacted password marker into the file.
# 4. Closes the file automatically and displays a success message.

# OR

# Q2) Write a Python program to implement a dictionary attack using a list of common passwords to check whether a target password exists in the list. [20 Marks]

common_passwords = [
    "123456",
    "password",
    "admin123",
    "welcome",
    "student123"
]

target_password = "admin123"

if target_password in common_passwords:
    print("Password found in the dictionary!")
else:
    print("Password not found in the dictionary.")


# Output:
# Password found in the dictionary!

# Working:
# 1. Creates a list containing common passwords.
# 2. Stores the sample target password in a variable.
# 3. Uses the in operator to check whether the target exists in the list.
# 4. Displays the appropriate message depending on the result.

# Requirements:
# Python 3; no external libraries or additional files are required.
# The first program automatically creates login_log.txt when executed.

# VIVA QUESTIONS AND ANSWERS - SLIP 1

# Q1. What is the CIA triad?
# Ans: CIA stands for Confidentiality, Integrity, and Availability.

# Q2. What is phishing?
# Ans: Phishing is a cyberattack that tricks users into revealing sensitive information.

# Q3. What is a dictionary attack?
# Ans: It tries passwords from a predefined list of common passwords.

# Q4. What is the purpose of file mode "a"?
# Ans: It opens a file in append mode and creates it if it does not exist.

# Q5. Why should passwords not be stored as plain text?
# Ans: Plain-text passwords can be exposed if the file is accessed by an unauthorized person.