from typing import List
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()


my_memos={
            "AdvProgCourse":"Do not forget projects" ,
            "JuneExams":"Study" ,
            "Vacations":"Make resrvations"
           }

@app.get("/")
async def root():
    return "Hello Advanced Programming....."



@app.get("/getNotes")
async def getNotes():
    return my_memos