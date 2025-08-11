#Imports the FastAPI class from the framework. I'll Instantiate this to create the web app.
from fastapi import FastAPI

''' -Creates the application object
    -This app is what Uvicorn will serve
'''
app = FastAPI(title ="Local Skills Map")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return{"message": "Hello Local Skills Map"}