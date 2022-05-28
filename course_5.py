from ast import Str
import json
import string
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()




@app.get("/")
async def root():
    return "Hello Advanced Programming....."






class Memo(BaseModel):
    Title: str
    Content: str



class Error(BaseModel):
    code: int
    reason: str



my_memos={
            "Title1":"Some notes for note 1.." ,
            "Title2":"Some notes for note 2.." ,
            "Title3":"Some notes for note 3.."
           }

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




#create a new memo
@app.post("/createNote",
    response_model=List[Memo], 
    responses={
        401: {"model": Error},
        422: {"model": Error}
        },
    tags=["WRITE"],
    summary="Create a new memo",
  )
async def insertNote(new_memo:Memo):
    print(new_memo.Title)
    if new_memo.Title in my_memos:
        error=Error(code=422,reason="This memo already exists")
        return JSONResponse(status_code=422, content={"code": error.code,"reason":error.reason})
    else:
        #append new memo in memo list
        my_memos[new_memo.Title]=new_memo.Content
        my_memos_list=list()
        for key, value in my_memos.items() :
            print (key, value)
            tmp_memo=Memo(Title=key,Content=value)
            my_memos_list.append(tmp_memo)
        return my_memos_list



#modify an existing memo
@app.patch("/modifyNote/{memo_title}",
    response_model=List[Memo], 
    responses={
        401: {"model": Error},
        422: {"model": Error}
        },
    tags=["WRITE"],
    summary="Modify an existing memo",
  )
async def modifyNote(memo_title, change_memo:Memo):
    if memo_title not in my_memos:
        error=Error(code=422,reason="No such memo")
        return JSONResponse(status_code=422, content={"code": error.code,"reason":error.reason})
    else:
        #modiy memo entry in memo list
        #check if title of new memo is the same
        if memo_title==change_memo.Title:
            #Same title update content
            my_memos[memo_title]=change_memo.Content
        else:
            #change Title,remove entry and create new one
            my_memos.pop(memo_title)
            my_memos[change_memo.Title]=change_memo.Content

        my_memos_list=list()
        for key, value in my_memos.items() :
            print (key, value)
            tmp_memo=Memo(Title=key,Content=value)
            my_memos_list.append(tmp_memo)
        return my_memos_list