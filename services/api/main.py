from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()


class Message(BaseModel):
    text = "Hello FastAPI"
    author = "John Does"


@app.get("/")
def hello():
    return {"message": "Hello FastAPI + SSL"}


@app.post("/")
def send_message(message: Message):
    text = message.text
    author = message.author
    response = {"status": "message received", "text": text, "author": author}
    return response
