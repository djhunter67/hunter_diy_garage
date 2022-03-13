from datetime import datetime

import fastapi
import fastapi_chameleon
import uvicorn
from colorama import Fore as F
from starlette.staticfiles import StaticFiles

R = F.RESET

from views import account, index

app = fastapi.FastAPI()


@app.on_event("shutdown")
def shutdown_event():
    dt_string = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    with open("logs/log/info.log", mode="a") as log:
        log.write(f"{dt_string}{F.YELLOW} Application shutdown{R}\n")


@app.on_event("startup")
def shutdown_event():
    dt_string = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    with open("logs/log/info.log", mode="a") as log:
        log.write(f"{dt_string}{F.GREEN} Application startup{R}\n")


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

    shutdown_event()


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
