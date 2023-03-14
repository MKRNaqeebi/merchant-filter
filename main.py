import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="res/static"), name="static")


templates = Jinja2Templates(directory="res/templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # read config.json into a dict
    with open("config.json") as f:
        config = json.load(f)
    # pass dict to template
    return templates.TemplateResponse("index.html", {"request": request, "id": 2, "config": config})
