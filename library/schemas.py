from pydantic import BaseModel


class Library(BaseModel):
    title: str
    description: str
    author:str