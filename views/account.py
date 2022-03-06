from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()

@app.get('/account')
def account():
    return {}

@app.get('/account/register')
def register():
    return {}

@app.get('/account/login')
def login():
    return {}
