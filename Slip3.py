# SLIP 3 – CYBER SECURITY

# Q1) What is phishing? Explain the step-by-step algorithm to identify phishing emails. [10 Marks]

# Definition:
# Phishing is a cyber attack in which attackers use fake emails, messages, or websites to trick users into revealing sensitive information such as passwords and banking details.

# Steps to Identify Phishing Emails:

# 1. Check the Sender:
# Verify the sender's email address and look for suspicious or unfamiliar addresses.

# 2. Check the Subject:
# Look for urgent or threatening subject lines that pressure the user to act quickly.

# 3. Check Links:
# Examine links carefully and verify that they lead to the correct official website.

# 4. Check the Message:
# Look for spelling mistakes, grammatical errors, and unusual requests for personal information.

# 5. Check Attachments:
# Avoid opening unexpected attachments because they may contain malicious software.

# 6. Verify the Request:
# Contact the organization through its official website or phone number if the email requests sensitive information.

# Conclusion:
# Identifying suspicious emails and verifying their authenticity helps prevent phishing attacks and protects personal information.


# Q2) Write a Python program to shift each alphabet by 2 positions. [20 Marks]

text = input("Enter a message: ")

result = ""

for ch in text:
    if ch.isupper():
        result += chr((ord(ch) - ord('A') + 2) % 26 + ord('A'))
    elif ch.islower():
        result += chr((ord(ch) - ord('a') + 2) % 26 + ord('a'))
    else:
        result += ch

print("Encrypted message:", result)

# Output:
# Enter a message: Hello World
# Encrypted message: Jgnnq Yqtnf

# Working:
# 1. Accepts a message from the user.
# 2. Checks whether each character is an uppercase or lowercase alphabet.
# 3. Uses ord() to obtain the character's ASCII value and shifts the alphabet by two positions.
# 4. Uses chr() to convert the new ASCII value back into a character.
# 5. The modulo operator (%) makes the shift wrap around, so Y becomes A and Z becomes B.
# 6. Non-alphabetic characters, including spaces and punctuation, remain unchanged.
# 7. Displays the final encrypted message.

# OR

# Q2) Write a Python program to simulate a phishing login page for educational purposes. [20 Marks]

print("=== Educational Login Simulation ===")

username = input("Enter demo username: ")
password = input("Enter demo password: ")

print("\nLogin simulation completed.")
print("Username entered:", username)
print("Password received: [REDACTED]")
print("Never enter real account credentials into an untrusted page.")

# Output:
# === Educational Login Simulation ===
# Enter demo username: student
# Enter demo password: test123
#
# Login simulation completed.
# Username entered: student
# Password received: [REDACTED]
# Never enter real account credentials into an untrusted page.

# Working:
# 1. Displays a message identifying the program as an educational simulation.
# 2. Accepts a demo username and password using input().
# 3. Displays the entered username and a redacted password marker.
# 4. Warns the user not to enter real account credentials into untrusted pages.
# 5. The program demonstrates how a fake login prompt can imitate a real login without saving the password to a file.

# Requirements:
# Python 3 is required.
# No external libraries or additional files are required.
# Both programs can run independently in VS Code or Jupyter Notebook.

# VIVA QUESTIONS AND ANSWERS - SLIP 3

# Q1. What is phishing?
# Ans: Phishing is a cyberattack that tricks users into revealing sensitive information.

# Q2. How can you identify a phishing email?
# Ans: Check the sender, suspicious links, urgent messages, and unexpected attachments.

# Q3. What are ord() and chr() in Python?
# Ans: ord() returns a character's numeric Unicode value, and chr() converts a number into a character.

# Q4. What is the purpose of the modulo (%) operator in the Caesar Cipher?
# Ans: It wraps alphabet shifts around from Z to A.

# Q5. Does the educational login simulation save the password?
# Ans: No, it displays a redacted password marker and does not save it to a file.