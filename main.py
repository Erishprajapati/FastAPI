from fastapi import FastAPI
from typing import Optional

app = FastAPI() #creating instance of the fastapi

@app.get('/blog') #this is the url when the url is clicked
def index(limit=10, published:bool = True, sort:Optional[str] = None):
    if published:#this is normal function
        return {'data': f'{limit} published blog list from the database'}
    else:
        return {'data': f'{limit} blog list from the database'}

@app.get('/blog/unpublished')
def unpublished_blog():
    return {'data': 'all unpublished blog'}

@app.get('/blog/{id}')
def getblogby_id(id:int):
    #fetching some particular blog
    return {'data' : id}

# @app.get('/about')
# def about():
#     return {"data": 'about page'}  

@app.get('/blog/{id}/comments')
def comments(id:int, limit = 10):
    return {'data':{'1','2','3','4','5','6','7','8','9','10','11','12'}}


@app.post('/blog')
def create_blog():
    return {'data' : "Blog created succesfully"}
