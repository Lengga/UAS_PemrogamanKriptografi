def encrypt_caesar(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Encrypt only alphabetic characters
            if char.islower():
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # Include non-alphabetic characters without encryption
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)
