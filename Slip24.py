# SLIP 24 – CYBER SECURITY

# Q1) What is a Man-In-The-Middle (MITM) attack? Explain common techniques used. [10 Marks]

# Answer:
#
# A Man-In-The-Middle (MITM) attack occurs when an attacker secretly
# intercepts communication between two parties and may read or modify
# the information exchanged between them.
#
# Common techniques used:
#
# 1. Wi-Fi Eavesdropping:
# An attacker monitors communication over an unsecured Wi-Fi network.
#
# 2. ARP Spoofing:
# An attacker sends fake ARP messages to associate their device with
# another device's IP address on a local network.
#
# 3. DNS Spoofing:
# An attacker provides false DNS information to redirect a user to
# a malicious website.
#
# 4. HTTPS Spoofing:
# An attacker attempts to trick users into visiting a fake website
# that appears trustworthy.
#
# 5. Session Hijacking:
# An attacker steals or misuses a user's session token to gain access
# to an active session.
#
# Prevention:
# Use HTTPS, avoid unsecured Wi-Fi for sensitive activities, keep
# devices updated, verify website addresses and certificates, and
# use secure network connections.


# Q2) Write a Python program to demonstrate IP tracking (simulation): Store fake IP addresses and print location mapping (use dictionary). [20 Marks]

ip_locations = {
    "192.168.1.10": "Pune",
    "192.168.1.20": "Mumbai",
    "192.168.1.30": "Delhi",
    "192.168.1.40": "Nashik"
}

print("IP Address and Location Mapping:")

for ip, location in ip_locations.items():
    print(ip, "->", location)

# Sample Output:
# IP Address and Location Mapping:
# 192.168.1.10 -> Pune
# 192.168.1.20 -> Mumbai
# 192.168.1.30 -> Delhi
# 192.168.1.40 -> Nashik

# Working:
# 1. Create a dictionary containing fake IP addresses as keys.
# 2. Store sample location names as their values.
# 3. Use a for loop to read each IP address and location.
# 4. Display the IP address and its mapped location.
# Note: This is a simulation using fake data, not real IP tracking.


# OR


# Q2) Write a simple Python program to hide a text message inside an image using steganography and display the hidden message again. [20 Marks]

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
# 4. Create a sample image and hide the binary bits in pixel values.
# 5. Save the image as secret_image.png.
# 6. Read the saved image and extract the hidden bits.
# 7. Convert the bits back into characters and display the message.

# Requirements:
# Python 3.
# Main Q2: no external libraries or files required.
# OR Q2: install Pillow using the command above.
# The OR program creates secret_image.png automatically.
# Run each Q2 program separately.
# Note: This demonstration supports ordinary ASCII text.

# VIVA QUESTIONS AND ANSWERS - SLIP 24

# Q1. What is a MITM attack?
# Ans: An attacker secretly intercepts communication between two parties.

# Q2. What is ARP spoofing?
# Ans: It uses fake ARP messages to mislead devices on a local network.

# Q3. What is IP tracking in this program?
# Ans: It displays predefined sample locations mapped to IP addresses.

# Q4. What is steganography?
# Ans: It hides secret information inside another file.

# Q5. Which Python library is used for image steganography?
# Ans: Pillow, imported using PIL.