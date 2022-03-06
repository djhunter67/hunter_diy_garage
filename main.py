import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get('/')
def index():

    return {
        "message": "hello fast_api"
    }

if __name__ == '__main__':
    uvicorn.run(app)
