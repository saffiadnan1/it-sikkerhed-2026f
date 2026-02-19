import os
import json
import flat_file_db


def setup_function():
    with open("db.json", "w") as f:
        json.dump({"users": []}, f)


def test_add_user_success():
    user = {
        "person_id": 1,
        "first_name": "Anna",
        "last_name": "Jensen",
        "address": "Main Street",
        "street_number": 10,
        "password": "secret123",
        "enabled": True
    }

    flat_file_db.add_user(user)
    result = flat_file_db.get_user(1)

    assert result is not None


def test_get_user_not_found():
    result = flat_file_db.get_user(999)
    assert result is None


def test_disable_user():
    user = {
        "person_id": 2,
        "first_name": "Peter",
        "last_name": "Nielsen",
        "address": "High Street",
        "street_number": 5,
        "password": "password",
        "enabled": True
    }

    flat_file_db.add_user(user)
    flat_file_db.disable_user(2)

    result = flat_file_db.get_user(2)
    assert result["enabled"] is False
    
    
    def test_pytest_works():
        assert 1 == 1

