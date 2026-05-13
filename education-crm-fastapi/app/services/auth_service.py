from app.auth.hashing import hash_password, verify_password
from app.auth.token import create_access_token


fake_users_db = []


def register_user(user):

    user["password"] = hash_password(user["password"])

    fake_users_db.append(user)

    return {
        "message": "User registered successfully"
    }


def login_user(email: str, password: str):

    for user in fake_users_db:

        if user["email"] == email:

            if verify_password(password, user["password"]):

                token = create_access_token(
                    {
                        "sub": user["email"],
                        "role": user["role"]
                    }
                )

                return {
                    "access_token": token,
                    "token_type": "bearer"
                }

    return None