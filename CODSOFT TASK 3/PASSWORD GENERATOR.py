import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use secrets module to generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length < 8:
            print("Password length should be at least 8 characters.")
            return
        password = generate_password(length)
        print("Generated Password: ", password)
    except ValueError:
        print("Please enter a valid number for password length.")

if __name__ == "__main__":
    main()