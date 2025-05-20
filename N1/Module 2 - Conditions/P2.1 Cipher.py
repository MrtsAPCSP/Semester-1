def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char.lower()) + shift
            if shifted > ord('z'):
                shifted -= 26
            encrypted += chr(shifted)
        else:
            encrypted += char
    return encrypted

def decrypt(encrypted_message, shift):
    return encrypt(encrypted_message, -shift)

# --- User Interaction ---
print("🔐 Caesar Cipher Encoder/Decoder")
choice = input("Would you like to encrypt or decrypt a message? ").lower()
message = input("Enter your message: ")
shift = int(input("Enter your shift number (1-25): "))

if choice == "encrypt":
    print("Encrypted message:", encrypt(message, shift))
elif choice == "decrypt":
    print("Decrypted message:", decrypt(message, shift))
else:
    print("Invalid choice.")
