from fastapi import FastAPI
app  = FastAPI()

@app.get('/home')
def main():
    return {"message": "hello this is main."} 

