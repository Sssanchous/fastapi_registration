from fastapi import FastAPI, HTTPException
from models import UserCreate, User

test_db = {}
user_counter = 1

app = FastAPI()

@app.post("/server1/register", response_model=User)
async def register_user(user: UserCreate):
    global user_counter

    if user.login in test_db:
        raise HTTPException(status_code=400, detail="Пользователь уже зарегестрирован")

    new_user = User(
        id=user_counter,
        name=user.name,
        surname=user.surname,
        login=user.login
    )

    test_db[user.login] = new_user
    user_counter += 1

    return new_user
