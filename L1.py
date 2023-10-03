from fastapi import FastAPI
from pydantic import BaseModel, Field
import wikipedia

app = FastAPI()


@app.get("/thing/{object}")
def find_object(object: str):
    return wikipedia.summary(object)

@app.get("/")
def main_info(object: str, count: int):
    return wikipedia.summary(object, sentences=count)

class Maket(BaseModel):
    gender: str
    info: list

class Input(BaseModel):
    name: str = Field(max_length=10)
    gender: str


@app.post("/person", response_model=Maket)
def person_info(input: Input):
    return {"gender": input.gender, "info": wikipedia.search(input.name)}

class coordinates(BaseModel):
    latitude: float
    longtitude: float

@app.post("/")
def coordinate(coord: coordinates):
    return wikipedia.geosearch(latitude=coord.latitude,
                               longitude=coord.longtitude,
                               results=5)