from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StudentModel(BaseModel):
    name: str
    height: float
    weight: float


@app.get('/hello')
async def hello():
    return 'hello world!'


@app.post('/student')
async def student(model: StudentModel):
    return model
