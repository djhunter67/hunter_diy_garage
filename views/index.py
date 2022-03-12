from fastapi import APIRouter
from starlette.requests import Request
from fastapi_chameleon import template

from viewmodels.index.indexviewmodel import IndexViewModel

router = APIRouter()


@router.get('/')
@template()
def index(request: Request):

    vm = IndexViewModel(request)

    return vm.to_dict()


@router.get("/about")
@template()
def about():
    return {}
