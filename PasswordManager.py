import base64
import json
import os
import secrets
from getpass import getpass

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# The plan
# 1. The first time you run it, you pick a master password.
# 2. The master password is turned into an encryption key (it is never saved).
# 3. Your passwords are kept in a dictionary like {"gmail": {"username": ..., "password": ...}}.
# 4. The dictionary is turned into text (JSON), encrypted, and saved in vault.dat.
# 5. Next time, the same master password makes the same key and unlocks the file.

VAULT_FILE = "vault.dat"
SALT_FILE = "vault.salt"

# The same levels as PasswordGenerator.py.
LEVELS = {
    "Easy": ("ABCDEFGHIJKL", 8),
    "Medium": ("ABCDEFGHIJKLMNOPQRSTUVWXYZ123", 12),
    "Hard": ("abcdefghijklmnopqrstuvwxyzABCDEFGHJKL12345!@#$", 16),
}


def make_key(master_password, salt):
    # PBKDF2 scrambles the master password many times, so guessing it is slow.
    # The salt is random bytes that make your key different from anyone else's.
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600_000,
    )
    key = kdf.derive(master_password.encode())
    # Fernet wants the key written in base64.
    return base64.urlsafe_b64encode(key)


def generate_password():
    # This is the Password Generator game turned into a function.
    # It uses secrets.choice instead of random.choice: random is fine for
    # games, but secrets is made for passwords and is much harder to guess.
    options = list(LEVELS)
    print(options)
    choice = input("Please select a level : ").strip().capitalize()
    while choice not in options:
        print("That's not a level. Please type Easy, Medium or Hard.")
        choice = input("Please select a level : ").strip().capitalize()

    characters, length = LEVELS[choice]
    password = ""
    i = 0
    while i < length:
        password = password + secrets.choice(characters)
        i = i + 1
    print(f"Generated password: {password}")
    return password


def ask_for_password():
    answer = input("Generate a password for you? (y/n): ").strip().lower()
    if answer == "y":
        return generate_password()
    return getpass("Password: ")


def save_vault(entries, fernet):
    text = json.dumps(entries)
    encrypted = fernet.encrypt(text.encode())
    with open(VAULT_FILE, "wb") as file:
        file.write(encrypted)


def load_vault(fernet):
    with open(VAULT_FILE, "rb") as file:
        encrypted = file.read()
    # If the master password is wrong, this line raises InvalidToken.
    text = fernet.decrypt(encrypted).decode()
    return json.loads(text)


def create_vault():
    print("No vault found. Let's make one.")
    while True:
        master = getpass("Choose a master password: ")
        again = getpass("Type it again: ")
        if master == "":
            print("The master password can't be empty. Try again.")
        elif master != again:
            print("The passwords did not match. Try again.")
        else:
            break

    salt = os.urandom(16)
    with open(SALT_FILE, "wb") as file:
        file.write(salt)

    fernet = Fernet(make_key(master, salt))
    entries = {}
    save_vault(entries, fernet)
    print("Vault created. Don't forget your master password, it can't be recovered!")
    return entries, fernet


def unlock_vault():
    with open(SALT_FILE, "rb") as file:
        salt = file.read()

    tries = 3
    while tries > 0:
        master = getpass("Master password: ")
        fernet = Fernet(make_key(master, salt))
        try:
            entries = load_vault(fernet)
            print("Vault unlocked.")
            return entries, fernet
        except InvalidToken:
            tries = tries - 1
            print(f"Wrong master password. {tries} tries left.")
    return None, None


def add_entry(entries, fernet):
    site = input("Site name: ").strip().lower()
    if site == "":
        print("The site name can't be empty.")
        return
    if site in entries:
        answer = input(f"{site} already exists. Replace it? (y/n): ").strip().lower()
        if answer != "y":
            return
    username = input("Username: ").strip()
    password = ask_for_password()
    entries[site] = {"username": username, "password": password}
    save_vault(entries, fernet)
    print(f"Saved {site}.")


def get_entry(entries):
    site = input("Site name: ").strip().lower()
    if site not in entries:
        print(f"No entry called {site}.")
        return
    entry = entries[site]
    print(f"Username: {entry['username']}")
    print(f"Password: {entry['password']}")


def list_entries(entries):
    if len(entries) == 0:
        print("The vault is empty.")
        return
    print("Saved sites:")
    for site in sorted(entries):
        print(f"- {site} ({entries[site]['username']})")


def search_entries(entries):
    word = input("Search for: ").strip().lower()
    found = []
    for site in sorted(entries):
        if word in site:
            found.append(site)
    if len(found) == 0:
        print(f"No sites match {word}.")
        return
    print("Matching sites:")
    for site in found:
        print(f"- {site} ({entries[site]['username']})")


def edit_entry(entries, fernet):
    site = input("Site name: ").strip().lower()
    if site not in entries:
        print(f"No entry called {site}.")
        return
    entry = entries[site]

    # Pressing Enter without typing keeps the old value.
    username = input(f"New username (Enter keeps {entry['username']}): ").strip()
    if username != "":
        entry["username"] = username

    answer = input("Change the password? (y/n): ").strip().lower()
    if answer == "y":
        entry["password"] = ask_for_password()

    save_vault(entries, fernet)
    print(f"Updated {site}.")


def change_master_password(entries, fernet):
    # Check it's really you before changing anything.
    with open(SALT_FILE, "rb") as file:
        salt = file.read()
    current = getpass("Current master password: ")
    try:
        load_vault(Fernet(make_key(current, salt)))
    except InvalidToken:
        print("That's not the current master password.")
        return fernet

    while True:
        new = getpass("New master password: ")
        again = getpass("Type it again: ")
        if new == "":
            print("The master password can't be empty. Try again.")
        elif new != again:
            print("The passwords did not match. Try again.")
        else:
            break

    # A new password gets a new salt, then everything is saved with the new key.
    new_salt = os.urandom(16)
    new_fernet = Fernet(make_key(new, new_salt))
    save_vault(entries, new_fernet)
    with open(SALT_FILE, "wb") as file:
        file.write(new_salt)
    print("Master password changed.")
    return new_fernet


def delete_entry(entries, fernet):
    site = input("Site name: ").strip().lower()
    if site not in entries:
        print(f"No entry called {site}.")
        return
    answer = input(f"Really delete {site}? (y/n): ").strip().lower()
    if answer == "y":
        del entries[site]
        save_vault(entries, fernet)
        print(f"Deleted {site}.")


def main():
    print("Welcome to the password manager")
    if os.path.exists(VAULT_FILE) and os.path.exists(SALT_FILE):
        entries, fernet = unlock_vault()
        if entries is None:
            print("Too many wrong tries. Goodbye.")
            return
    else:
        entries, fernet = create_vault()

    options = ["Add", "Get", "List", "Search", "Edit", "Delete", "Generate", "Master", "Quit"]
    while True:
        print()
        print(options)
        choice = input("Please select an option : ").strip().capitalize()
        if choice == "Add":
            add_entry(entries, fernet)
        elif choice == "Get":
            get_entry(entries)
        elif choice == "List":
            list_entries(entries)
        elif choice == "Search":
            search_entries(entries)
        elif choice == "Edit":
            edit_entry(entries, fernet)
        elif choice == "Generate":
            generate_password()
        elif choice == "Master":
            fernet = change_master_password(entries, fernet)
        elif choice == "Delete":
            delete_entry(entries, fernet)
        elif choice == "Quit":
            print("Goodbye.")
            break
        else:
            print("That's not an option. Please pick one from the list.")


if __name__ == "__main__":
    main()
