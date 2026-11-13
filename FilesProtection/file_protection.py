from cryptography.fernet import Fernet, InvalidToken
import os


# Generate encryption key
def generate_key():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    print("Encryption key generated successfully!")


# Load encryption key
def load_key():
    return open("secret.key", "rb").read()


# Encrypt file
def encrypt_file(filename):

    if not os.path.exists(filename):
        print("File not found!")
        return

    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")
    print("Saved as:", filename + ".encrypted")


# Decrypt file
def decrypt_file(filename):

    if not os.path.exists(filename):
        print("Encrypted file not found!")
        return

    key = load_key()
    fernet = Fernet(key)

    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        original_name = filename.replace(".encrypted", "")

        with open(original_name + ".restored", "wb") as file:
            file.write(decrypted_data)

        print("File decrypted successfully!")
        print("Restored file:", original_name + ".restored")

    except InvalidToken:
        print("Invalid key or corrupted encrypted file!")


# Main program
while True:

    print("\n===== FILE PROTECTION UTILITY =====")
    print("1. Generate Encryption Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        filename = input("Enter file name: ")
        encrypt_file(filename)

    elif choice == "3":
        filename = input("Enter encrypted file name: ")
        decrypt_file(filename)

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")