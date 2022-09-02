from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    username: str
    password: str
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Bangui"}

@app.get("/posts")
def get_posts():
    return {"data":"This is your post"}

@app.post("/createposts")
def create_posts(post:Post):
    return {"data":post}