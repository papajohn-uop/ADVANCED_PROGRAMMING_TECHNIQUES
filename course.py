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


@app.get("/getNote/{memo_title}",
    response_model=Memo, 
    responses={
        401: {"model": Error},
        404: {"model": Error}
        },
    tags=["READ"],
    summary="List a specific memo",
  )
async def getNote(memo_title):
    if memo_title in my_memos:
        selected_memo=Memo(Title=memo_title,Content=my_memos[memo_title])
        return selected_memo
    else:
        error=Error(code=404,reason="This memo does not exist")
        return JSONResponse(status_code=404, content={"code": error.code,"reason":error.reason})
