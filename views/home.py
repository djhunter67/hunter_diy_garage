from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()


@app.get('/')
@template(template_file='home/index.html')
def index(user: str = 'anon'):
    
    return {
        "user_name": user
    }

@app.get("/about")
def about():
    return {}