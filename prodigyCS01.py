def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            # Shift the letter and wrap around alphabet
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char  #Keep spaces and punctuation unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  #Just reverse the shift

# Main program
print(" Caesar Cipher Tool ")
choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))

if choice == 'e':
    encrypted = encrypt(message, shift)
    print(" Encrypted message:", encrypted)
elif choice == 'd':
    decrypted = decrypt(message, shift)
    print(" Decrypted message:", decrypted)
else:
    print("❌ Invalid choice. Please enter 'E' or 'D'.")
