from fastapi import FastAPI
# import requests
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
from pydantic import BaseModel
from bson.json_util import dumps, loads
from fastapi.responses import JSONResponse
from mongo import mongo_uri

app = FastAPI()
uri = mongo_uri
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Links"]
collection = db["link-info"]


class Link(BaseModel):
    social_media: str = None
    link: str = None
    Note: str = None


@app.get('/')
async def home():

    return {"message": "home is working properlly"}


@app.get('/check')
async def check():

    return {"message": "this is a check message for deployment testing"}


@app.get('/links')
async def get_links():
    try:
        # Retrieve and process documents
        data = collection.find({})
        documents = []
        for doc in data:
            doc.pop("_id", None)  # Remove _id field if it exists
            documents.append(doc)

        if not documents:
            return {"message": "No data found"}
        return {"links": documents}
    except Exception as e:
        return {"error occurred": str(e)}


@app.post('/save-links')
async def save_link(links: Link):  # update/create

    try:
        collection.insert_one(links)
        print("create operation succssful")
        return {"message": "your link is saved propoerlly", "hear is the data saved for reference": links}
    except:
        print(Exception)
        return {"error": Exception}
