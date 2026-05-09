from fastapi import FastAPI
from pydantic import BaseModel
from storage import add_user, get_all_users

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    number: int

@app.get("/")
def root():
    return{"message": "API is running"}

@app.get("/users")
def get_users():
    return get_all_users()

@app.post("/users")
def create_users(user:User):
    user_dict = user.dict()
    add_user(user_dict)
    return {"message": "User added", "user": user_dict}