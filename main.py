import json
import getpass
from cryptography.fernet import Fernet
def generate_key():
    return Fernet.generate_key()
def encrypt_password(password, key):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

def save_passwords(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
def load_passwords(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}

def main():
    key = generate_key()
    password_data = load_passwords('passwords.json')

    while True:
        print("\nPassword Manager Menu:")
        print("1. Store a new password")
        print("2. Retrieve a password")
        print("3. Show all stored passwords")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            website = input("Enter website or app name: ")
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            print(password)

            encrypted_password = encrypt_password(password, key)
            if website not in password_data:
                password_data[website] = {'username': username, 'password': encrypted_password}
            else:
                print("Password for this website already exists. Please use option 2 to retrieve/update.")

            save_passwords(password_data, 'passwords.json')
            print("Password stored successfully!")

        elif choice == '2':
            website = input("Enter website or app name: ")
            if website in password_data:
                stored_password = password_data[website]['password']
                decrypted_password = decrypt_password(stored_password, key)
                print(f"Username: {password_data[website]['username']}")
                print(f"Password: {decrypted_password}")
            else:
                print("Password not found for this website.")

        elif choice == '3':
            print("Stored Passwords:")
            for website, data in password_data.items():
                print(f"Website/App: {website} | Username: {data['username']}")

        elif choice == '4':
            print("Exiting Password Manager. Have a great day!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()