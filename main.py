import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/js", StaticFiles(directory="frontend/dist/js"), name="static")
app.mount("/css", StaticFiles(directory="frontend/dist/css"), name="static")
app.mount("/img", StaticFiles(directory="frontend/dist/img"), name="static")
app.mount("/fonts", StaticFiles(directory="frontend/dist/fonts"), name="static")
# app.mount("/favicon.ico", StaticFiles(directory="frontend/dist"), name="static")

templates = Jinja2Templates(directory="frontend/dist")

# rest api to get config
@app.get("/config")
async def read_item():
    # read json file into dict
    with open("config.json") as f:
        dict_data = json.load(f)
    return dict_data

@app.get("/items/{store_id}")
def read_item(store_id: int):
    return {"item_id": store_id}

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # pass dict to template
    return templates.TemplateResponse("index.html", {"request": request})

# uvicorn main:app --reload
