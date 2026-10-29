# SLIP 25 – CYBER SECURITY

# Q1) What is phishing? Explain the step-by-step algorithm to identify phishing emails. [10 Marks]

# Answer:
#
# Phishing is a cyberattack in which an attacker sends fake emails or
# messages to trick users into revealing sensitive information, such as
# passwords, bank details, or OTPs.
#
# Step-by-step algorithm to identify phishing emails:
#
# Step 1: Receive the email.
# Step 2: Check the sender's email address for suspicious spelling
#         or an unknown domain.
# Step 3: Read the subject and message for urgent or threatening words.
# Step 4: Check links carefully without opening suspicious links.
# Step 5: Look for spelling mistakes, unusual attachments, and requests
#         for passwords or financial information.
# Step 6: Verify the message through the official website or contact
#         details of the organization.
# Step 7: If the email appears suspicious, do not click its links or
#         download attachments. Report it as phishing.
#
# Prevention:
# Use spam filters, enable multi-factor authentication, keep software
# updated, and never share passwords or OTPs through email.


# Q2) Write a simple Python program to hide a text message inside an image and display the hidden message again. [20 Marks]

# Install the required library:
# python -m pip install pillow

from PIL import Image

message = input("Enter secret message: ")
binary = ''.join(format(ord(ch), '08b') for ch in message) + '00000000'

image = Image.new("RGB", (100, 100), "white")
pixels = image.load()

if len(binary) > image.width * image.height * 3:
    print("Message is too long.")
else:
    index = 0

    for y in range(image.height):
        for x in range(image.width):
            if index >= len(binary):
                break

            r, g, b = pixels[x, y]
            values = [r, g, b]

            for i in range(3):
                if index < len(binary):
                    values[i] = (values[i] & 254) | int(binary[index])
                    index += 1

            pixels[x, y] = tuple(values)

        if index >= len(binary):
            break

    image.save("secret_image.png")

    hidden_image = Image.open("secret_image.png").convert("RGB")
    hidden_pixels = hidden_image.load()
    extracted_bits = ""

    for y in range(hidden_image.height):
        for x in range(hidden_image.width):
            for value in hidden_pixels[x, y]:
                extracted_bits += str(value & 1)

    decoded = ""

    for i in range(0, len(extracted_bits), 8):
        byte = extracted_bits[i:i + 8]

        if len(byte) < 8 or byte == "00000000":
            break

        decoded += chr(int(byte, 2))

    print("Hidden message:", decoded)

# Sample Output:
# Enter secret message: Hello
# Hidden message: Hello

# Working:
# 1. Accept a secret message from the user.
# 2. Convert each character into 8-bit binary.
# 3. Add a zero-byte marker to identify the end of the message.
# 4. Create an image and hide the binary bits in its pixel values.
# 5. Save the image as secret_image.png.
# 6. Open the saved image and extract the hidden bits.
# 7. Convert the bits back into characters and display the message.


# OR


# Q2) Write a Python program to simulate a phishing login page for educational purposes. [20 Marks]

print("===== Educational Login Simulation =====")

username = input("Enter demo username: ")
password = input("Enter demo password: ")

if username and password:
    print("Demo login submitted.")
    print("Username entered:", username)
    print("Password: [HIDDEN]")
    print("This is only an educational simulation.")
else:
    print("Username and password cannot be empty.")

# Sample Output:
# ===== Educational Login Simulation =====
# Enter demo username: student
# Enter demo password: demo123
# Demo login submitted.
# Username entered: student
# Password: [HIDDEN]
# This is only an educational simulation.

# Working:
# 1. Display a simulated login message.
# 2. Accept a demo username and password.
# 3. Check whether both fields contain values.
# 4. Display the username and hide the password in the output.
# 5. Show a message confirming that this is an educational simulation.
# Note: This program does not save or transmit credentials.

# Requirements:
# Python 3.
# Main Q2: install Pillow using the command above.
# The image program creates secret_image.png automatically.
# OR Q2: no external libraries or files are required.
# Run each Q2 program separately.
# The image program supports ordinary ASCII text.

# VIVA QUESTIONS AND ANSWERS - SLIP 25

# Q1. What is phishing?
# Ans: Phishing is a cyberattack that tricks users into revealing sensitive information.

# Q2. How can you identify a phishing email?
# Ans: Check the sender, suspicious links, urgent language, and unusual attachments.

# Q3. What is steganography?
# Ans: It hides secret information inside another file.

# Q4. Which library is used for image steganography?
# Ans: Pillow, imported using PIL.

# Q5. Why is the login program called a simulation?
# Ans: It demonstrates a login process without saving or transmitting credentials.