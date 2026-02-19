import json
import bcrypt
from cryptography.fernet import Fernet

DB_FILE = "db.json"
KEY_FILE = "secret.key"


def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()


def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def encrypt_data(data: str) -> bytes:
    f = Fernet(load_key())
    return f.encrypt(data.encode())


def decrypt_data(token: bytes) -> str:
    f = Fernet(load_key())
    decrypted = f.decrypt(token).decode()
    return decrypted


def add_user(user):
    db = load_db()

    user["password"] = hash_password(user["password"]).decode()
    user["address"] = encrypt_data(user["address"]).decode()

    db["users"].append(user)
    save_db(db)


def get_user(person_id):
    db = load_db()

    for user in db["users"]:
        if user["person_id"] == person_id:
            user_copy = user.copy()
            user_copy["address"] = decrypt_data(user["address"].encode())
            return user_copy

    return None

def disable_user(person_id):
    db = load_db()

    for user in db["users"]:
        if user["person_id"] == person_id:
            user["enabled"] = False
            save_db(db)
            return True

    return False

