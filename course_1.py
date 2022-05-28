from typing import List
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()


@app.get("/")
async def root():
    return "Hello Advanced Programming....."