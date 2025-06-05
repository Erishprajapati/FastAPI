from fastapi import FastAPI

app = FastAPI() #creating instance of the fastapi

@app.get('/')
def index():
    return {'data':{'name' : "erish"}}

@app.get('/about')
def about():
    return {"data": 'about page'}  