from fastapi import FastAPI
import requests
from pydantic import BaseModel
app = FastAPI()


class Link(BaseModel):
    social_Media: str = None
    link: str = None
    Note: str = None


@app.get('/')
def home():

    return {"message": "home is working properlly"}


@app.get('/check')
def check():

    return {"message": "this is a check message for deployment testing"}


@app.get('/links')
def get_links(url, note):

    return {"Note": note, "url": url}


@app.post('/save-links')
async def save_link(links: Link):
    return {"message": "it is working", "data": links}
