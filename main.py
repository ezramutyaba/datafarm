from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Bangui"}

@app.get("/posts")
def get_posts():
    return {"data":"This is your post"}

@app.post("/createposts")
def create_posts():
    return {"data":"nothimg"}