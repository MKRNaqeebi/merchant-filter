import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

app.mount("/js", StaticFiles(directory="frontend/dist/js"), name="static")
app.mount("/css", StaticFiles(directory="frontend/dist/css"), name="static")
# app.mount("/img", StaticFiles(directory="frontend/dist/img"), name="static")
app.mount("/fonts", StaticFiles(directory="frontend/dist/fonts"), name="static")
# app.mount("/favicon.ico", StaticFiles(directory="frontend/dist"), name="static")

templates = Jinja2Templates(directory="frontend/dist")


class InputType(BaseModel):
    inputtype: str
    store: int

# rest api to get config
@app.get("/api/config")
async def read_item():
    # read json file into dict
    with open("config.json") as f:
        dict_data = json.load(f)
    return dict_data

@app.get("/api/stores/{store_id}")
def read_store(store_id: int):
    print(store_id)
    return {"item_id": store_id}

# post store data
@app.post("/api/stores")
def create_store(input_type: InputType):
    # get data from request
    print(input_type)
    return {"item_id": input_type.store, "input_type": input_type.inputtype}

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # pass dict to template
    return templates.TemplateResponse("index.html", {"request": request})

# uvicorn main:app --reload
