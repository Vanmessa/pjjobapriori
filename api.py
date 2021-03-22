from tensorflow.keras.models import load_model
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
import sqlite3
import csv
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import json


app = FastAPI()

class Data(BaseModel):
    Act:str
    # x:float
    # y:float



def db_connect():
    con = sqlite3.connect('apriori.sqlite3')
    print("connect success")
    return con

async def predict(data):
    con=db_connect()
# con.row_factory = dict_factory
    cur= con.cursor()
    
    cur.execute("SELECT * FROM merge2")
    data1=cur.fetchall()
# type(data1)
# data1
# dict1={}
# dict1=data1.to_dict('index')
# dict1
    d = {}
    for key, val in data1:
        d.setdefault(key, []).append(val)

    # print(d)
    # json_object = json.dumps(d, ensure_ascii=False)
    # n=data.UserID
    Act2=data.Act
    n = data.Act
    dor=d.get(n)

    return  Act2,dor 

@app.post("/getclass/")
async def get_class(data: Data):
    # category, confidence = await predict(data)
    # res = {'class': category, 'confidence':confidence}

    Act2,dor = await predict(data)
    res = { 'Act':Act2,'dormitory':dor}
    return {'results': res}

