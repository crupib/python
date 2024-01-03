# static_img.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/imgs", StaticFiles(directory="imgs"), name='images')

@app.get("/", response_class=HTMLResponse)
def serve():
    return """
    <html>
        <head>
            <title></title>
        </head>
        <body>
        <img src="imgs/g.png">
        <h1>Hello World</h1>
        </body>
    </html>
    """
