import hashlib

def hash_password(password):
    # Generate a salt (you can use a cryptographically secure random generator)
    salt = "SALT_VALUE"

    # Concatenate the salt and password
    salted_password = salt + password

    # Hash the salted password using SHA-256
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

    return hashed_password

# Example usage
password = input("Enter a password: ")
hashed_password = hash_password(password)
print("Hashed password:", hashed_password)
