from fastapi import FastAPI
# import win32com.client
import requests

app  = FastAPI()
@app.get('/')

@app.get('/home')
def main():
    return {"message": "hello this is main."} 

    # importing requests package

@app.get('/bbc')
def NewsFromBBC():

    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "fae7a52a71f742db93a9e41ed1b91b37"
    }
    main_url = " https://newsapi.org/v1/articles"
    # https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=fae7a52a71f742db93a9e41ed1b91b37

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])
    
    # from win32com.client import Dispatch
    # speak = Dispatch("SAPI.Spvoice")
    # speak.Speak(results)

    return {"message": results}

# def reader():

