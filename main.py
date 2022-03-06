import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get('/')
def index():
    content = """
    <h1 style="color: blue"> FASTAPI project </h1>

    <p> by Christerpher Hunter </p>
    """
    return fastapi.responses.HTMLResponse(content)

if __name__ == '__main__':
    uvicorn.run(app)