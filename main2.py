from fastapi import FastAPI
from controllers.utills import read_item_block

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}


@app.get("/blocks/{block_id}")
def read_item(block_id: int, query_param_lol: str = None):
    return read_item_block(block_id,query_param_lol)
