import json

DB_FILE = "db.json"


def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_user(user):
    db = load_db()
    db["users"].append(user)
    save_db(db)


def get_user(person_id):
    db = load_db()
    for user in db["users"]:
        if user["person_id"] == person_id:
            return user
    return None


def disable_user(person_id):
    db = load_db()
    for user in db["users"]:
        if user["person_id"] == person_id:
            user["enabled"] = False
            save_db(db)
            return True
    return False
