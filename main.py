from turtle import home
from fastapi_chameleon import  global_init
import fastapi
import uvicorn
from views import
from views import (
    home,
    account,
)

app = fastapi.FastAPI()
global_init('templates')


app.include_router(home.router)
app.include_router(account.router)


if __name__ == '__main__':
    uvicorn.run(app)