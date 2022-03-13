from fastapi import APIRouter
from starlette.requests import Request
from fastapi_chameleon import template

from viewmodels.index.indexviewmodel import AccountViewModel

router = APIRouter()

@router.get('/account')
@template()
def account(request: Request):
    
    vm = AccountViewModel(request)

    return vm.to_dict()

@router.get('/account/register')
def register():
    return {}

@router.get('/account/login')
def login():
    return {}
