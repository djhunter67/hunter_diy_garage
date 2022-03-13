from concurrent.futures import thread
from views import account, index
from datetime import datetime

import fastapi
import fastapi_chameleon
import uvicorn
from colorama import Fore as F
from starlette.staticfiles import StaticFiles
import logging

R = F.RESET


app = fastapi.FastAPI()


@app.on_event("shutdown")
def shutdown_event():
    dt_string = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    with open("logs/log/logFile.log", encoding="utf-8", mode="a") as log:
        log.write(
            f"{F.CYAN}USER_INFO:{R} {dt_string}{F.YELLOW} Application shutdown{R}\n")


@app.on_event("startup")
def shutdown_event():
    dt_string = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    with open("logs/log/logFile.log", encoding="utf-8", mode="a") as log:
        log.write(
            f"{F.CYAN}USER_INFO:{R} {dt_string}{F.GREEN} Application startup{R}\n")


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

    logging.basicConfig(
        filename="logs/log/logFile.log",
        encoding='utf-8',
        level=logging.WARNING,
        format="%(asctime)s %(message)s",
        datefmt=f"{datetime.now().strftime('%d/%b/%Y %H:%M:%S')}")

    logging.exception=True

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
