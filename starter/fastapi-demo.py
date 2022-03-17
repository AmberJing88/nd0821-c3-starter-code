# the demo of the fastapi 
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Value(BeseModel):
    value: int
        
        
@app.post("/{path}")
async def exercise_function(path: int, query:int, body:Value):
    return {"path": path, "query":query, "body": body}


@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"fetch": f"Fetched {count} of {item_id}"}

