from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit=10, published: bool=True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published Blog from the db'}
    else:
        return {'data': f'{limit} Blog from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id,  limit=10):
    #fetch comments of blog with id = id
    return{'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published_by: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f"blog is created with title as {request.title}"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)

#Request Body
#How to Debug
#Press Control Shift&P (ctrl/shift&p), Debug, Start, language
#Pydantic Schema
#DataBase Connection
#Model & Table
#Store Blog to Database
#Get Blog From Database
#Exception & Status code
#Delete A Blog
#Update a Blog
#Create User
#Hash the Password
#Show a User