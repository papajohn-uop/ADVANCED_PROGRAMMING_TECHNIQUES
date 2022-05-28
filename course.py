from typing import List
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List


class Memo(BaseModel):
    Title: str
    Content: str

class Error(BaseModel):
    code: int
    reason: str


app = FastAPI()


my_memos={
            "AdvProgCourse":"Do not forget projects" ,
            "JuneExams":"Study" ,
            "Vacations":"Make resrvations"
           }

@app.get("/")
async def root():
    return "Hello Advanced Programming....."



@app.get("/getNotes",
    response_model=List[Memo], 
    responses={404: {"model": Error}},
    tags=["READ"],
    summary="List current memos",

)
async def getNotes():
    my_memos_list=list()
    for key, value in my_memos.items() :
        print (key, value)
        tmp_memo=Memo(Title=key,Content=value)
        my_memos_list.append(tmp_memo)
    return my_memos_list