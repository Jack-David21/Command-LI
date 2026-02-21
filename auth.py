import hashlib
import getpass
from storage import load_users, save_users


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def is_valid_username(username):
    allowed = "abcdefghijklmnopqrstuvwxyz0123456789_"
    return (
        5 <= len(username) <= 10 and
        all(c in allowed for c in username) and
        username.count("_") <= 5
    )

def register_user():
    users = load_users()
    while True:
        username = input("Enter username: ").lower()
        if not is_valid_username(username):
            print("Invalid username.")
            continue
        if username in users:
            print("Username already exists.")
            continue
        break
    while True:
        password = getpass.getpass("Enter password: ")
        if len(password) < 6:
            print("Password too short.")
            continue            
        break

    users[username] = {
    "password": hash_password(password),
    "todos": []
}

    save_users(users)
    print("Registration successful.")   
    print(f"Welcome, {username}!")

def login_user():
    users = load_users()
    while True:
        username = input("Enter username: ").lower()
        if username in users:
            break
        print("Username does not exist.")
    attempts = 3
    while attempts > 0:
        password = getpass.getpass("Enter password: ")
        hashed = hash_password(password)

        if users[username]["password"] == hashed:
            print(f"Welcome back, {username}!")
            return username
        else:
            attempts -= 1
            print(f"Incorrect password. Attempts left: {attempts}")
    print("Too many failed attempts.")
    return None