from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    surname: str
    login: str
    password: str


class User(BaseModel):
    id: int
    name: str
    surname: str
    login: str
