# SLIP 12 – CYBER SECURITY

# Q1) What specific digital evidence can be obtained from browser history analysis in digital forensics? [10 Marks]

# Definition:
# Browser history analysis is a digital forensic technique used to examine browser records and identify a user's browsing activities during an investigation.

# Types of Digital Evidence:

# 1. Visited Websites:
# Browser history contains URLs of websites visited by a user.

# 2. Date and Time:
# Timestamps help investigators determine when websites were accessed.

# 3. Downloaded Files:
# Download history may contain file names, download locations, and download times.

# 4. Search Queries:
# Search records may reveal the terms entered by a user in a search engine.

# 5. Cookies and Session Data:
# Cookies may provide information about website sessions and user preferences.

# 6. Cached Data:
# Cached files may contain copies of website resources stored by the browser.

# 7. Bookmarks:
# Bookmarks show websites saved by the user for future reference.

# Conclusion:
# Browser history analysis helps investigators reconstruct browsing activities and identify useful digital evidence. However, records may be deleted or modified.


# Q2) Write a simple Python program to hide a text message inside an image and display the hidden message again. [20 Marks]

# Install library in terminal:
# python -m pip install pillow

from PIL import Image

message = input("Enter a secret message: ")
binary = ''.join(format(ord(ch), '08b') for ch in message + chr(0))

image = Image.new("RGB", (200, 200), "white")
pixels = image.load()

if len(binary) > image.width * image.height * 3:
    print("Message is too long!")
else:
    index = 0

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            values = [r, g, b]

            for i in range(3):
                if index < len(binary):
                    values[i] = (values[i] & 254) | int(binary[index])
                    index += 1

            pixels[x, y] = tuple(values)

            if index >= len(binary):
                break
        if index >= len(binary):
            break

    image.save("secret_image.png")

    hidden_image = Image.open("secret_image.png").convert("RGB")
    decoded_bits = ""

    for y in range(hidden_image.height):
        for x in range(hidden_image.width):
            for value in hidden_image.getpixel((x, y)):
                decoded_bits += str(value & 1)

    decoded = ""

    for i in range(0, len(decoded_bits), 8):
        byte = decoded_bits[i:i + 8]

        if len(byte) < 8:
            break

        ch = chr(int(byte, 2))

        if ch == chr(0):
            break

        decoded += ch

    print("Hidden message:", decoded)
    print("Image saved as secret_image.png")

# Output:
# Enter a secret message: Hello
# Hidden message: Hello
# Image saved as secret_image.png

# Working:
# 1. Accepts a secret message and converts each character into 8-bit binary.
# 2. Adds a null character to mark the end of the message.
# 3. Creates a white RGB image and checks whether the message fits.
# 4. Hides the binary bits in the least significant bits of the image's RGB values.
# 5. Saves the image as secret_image.png.
# 6. Opens the saved image and extracts the hidden bits.
# 7. Converts the bits back into characters and stops at the null character.
# 8. Displays the recovered message.

# OR

# Q2) Calculate and encrypt the number M = 5 using the RSA algorithm given p = 3, q = 11, and e = 7. [20 Marks]

p = 3
q = 11
e = 7
M = 5

n = p * q
phi = (p - 1) * (q - 1)

d = pow(e, -1, phi)

C = pow(M, e, n)
decrypted = pow(C, d, n)

print("n =", n)
print("Phi(n) =", phi)
print("Public key =", (e, n))
print("Private key =", (d, n))
print("Encrypted message =", C)
print("Decrypted message =", decrypted)

# Output:
# n = 33
# Phi(n) = 20
# Public key = (7, 33)
# Private key = (3, 33)
# Encrypted message = 14
# Decrypted message = 5

# Working:
# 1. Calculates n = p * q = 3 * 11 = 33.
# 2. Calculates phi(n) = (p - 1) * (q - 1) = 20.
# 3. Finds d = 3 because (e * d) mod phi(n) = 1.
# 4. Encrypts M using C = M^e mod n = 5^7 mod 33 = 14.
# 5. Decrypts C using M = C^d mod n = 14^3 mod 33 = 5.
# 6. Displays the public key, private key, ciphertext, and decrypted message.

# Requirements:
# Python 3 is required.
# Main program: Install Pillow using python -m pip install pillow.
# No external image is required; secret_image.png is created automatically.
# OR program: No external libraries or files are required.
# RSA uses small values for educational purposes only.

# VIVA QUESTIONS AND ANSWERS - SLIP 12

# Q1. What is browser history analysis?
# Ans: It is a digital forensic technique used to examine a user's browsing activities.

# Q2. What information can browser history provide?
# Ans: It can provide visited URLs, timestamps, downloads, and search queries.

# Q3. What is steganography?
# Ans: It is the technique of hiding secret information inside another file, such as an image.

# Q4. What is the purpose of the Pillow library?
# Ans: Pillow is a Python library used to create, open, and modify images.

# Q5. What is RSA?
# Ans: RSA is a public-key cryptographic algorithm used for encryption and decryption.