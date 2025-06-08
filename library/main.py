from fastapi import FastAPI
import schemas

app = FastAPI()



@app.post('/library')
def create(request: schemas.Library):
    return request