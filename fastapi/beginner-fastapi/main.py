from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


fake_items_db = [{"item_name": "foo"}, {
    "item_name": "bar"}, {"item_name": "baz"}]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "The current user"}

# path params


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "deep learning FTW"}
    elif model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    else:
        return {"model_name": model_name, "message": "Have some residual."}


@app.get("/files/{file_path:path}")
async def get_file(file_path: str):
    return {"file_path": file_path}


# query params

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]
