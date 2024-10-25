from fastapi import FastAPI
# import win32com.client
import requests

app = FastAPI()


@app.get('/')
def home():
    requests
    return {"message": "another home"}


@app.get('/home')
def main():
    return {"message": "hello this is main."}
