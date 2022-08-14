# api-in-10-min
1. Create virtual environment
```commandline
python -m venv venv 
```
2. Get in venv
```commandline
source venv/bin/activate 
```
3. Install packages
```commandline
pip install uvicorn gunicorn fastapi pydantic
```
4. Create & save api.py
```commandline
touch api.py
```
```python
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

```
5. Run server
```commandline
uvicorn api:app --reload
```

### Bonus : Upload to Heroku
1. Export packages
```commandline
pip freeze > requirments.txt
```
2. Create & save .gitignore
```commandline
touch .gitignore
```
```gitignore
__pycache__
venv
.idea
```
3. Create & save Procfile
```commandline
touch Procfile
```
```text
web: gunicorn -w 2 -k uvicorn.workers.UvicornWorker api:app
```
4. Create & save runtime.txt (check your python version & save it as runtime)
```commandline
python --version
touch runtime.txt
```
```text
python-3.9.12
```
5. Initial Git
```commandline
git init
git add .
git commit -m "Initial commit."
```
6. Upload to Heroku
```commandline
heroku login
heroku create
git push heroku master
```
