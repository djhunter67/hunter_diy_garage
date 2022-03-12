import fastapi
import fastapi_chameleon
import uvicorn
from starlette.staticfiles import StaticFiles

from views import account, index

app = fastapi.FastAPI()


def main():

    configure()
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=8000,
                workers=2,
                reload=True,
                )


def configure():

    configure_templates()
    configure_routes()

    favicon_path = "favicon.ico"

    @app.get("/favicon.ico")
    def favicon():
        return fastapi.responses.FileResponse(favicon_path)


def configure_templates():

    fastapi_chameleon.global_init("templates")


def configure_routes():

    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(index.router)
    app.include_router(account.router)


if __name__ == "__main__":
    main()
else:
    configure()
