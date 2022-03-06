import fastapi
import fastapi_chameleon
import uvicorn

from views import account, home

app = fastapi.FastAPI()


def main():

    configure()
    uvicorn.run(app, host='127.0.0.1', port=8000)


def configure():

    configure_templates()
    configure_routes()


def configure_templates():

    fastapi_chameleon.global_init('templates')


def configure_routes():

    app.include_router(home.router)
    app.include_router(account.router)


if __name__ == '__main__':
    main()
else:
    configure()
