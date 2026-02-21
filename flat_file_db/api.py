from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import flat_file_db

app = FastAPI(title="Flat File DB API")


class User(BaseModel):
    person_id: int
    first_name: str
    last_name: str
    address: str
    street_number: int
    password: str
    enabled: bool = True


# CREATE
@app.post("/users")
def create_user(user: User):
    flat_file_db.add_user(user.dict())
    return {"message": "User created"}


# READ
@app.get("/users/{person_id}")
def get_user(person_id: int):
    user = flat_file_db.get_user(person_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# UPDATE
@app.put("/users/{person_id}")
def disable_user(person_id: int):
    success = flat_file_db.disable_user(person_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User disabled"}


# DELETE
@app.delete("/users/{person_id}")
def delete_user(person_id: int):
    db = flat_file_db.load_db()
    users = db["users"]

    new_users = [u for u in users if u["person_id"] != person_id]
    if len(users) == len(new_users):
        raise HTTPException(status_code=404, detail="User not found")

    db["users"] = new_users
    flat_file_db.save_db(db)
    return {"message": "User deleted"}


# LIST
@app.get("/users")
def list_users():
    db = flat_file_db.load_db()
    return db["users"]