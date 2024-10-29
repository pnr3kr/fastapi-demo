#!/usr/bin/env python3

from fastapi import Request, FastAPI
from typing import Optional
from pydantic import BaseModel
import pandas as pd 
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Hi": "TD!"}

@app.get("/sum/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
    return {"product": c * d}

@app.get("/square/{a}")
async def square(a: int):
    return {"square": a * a}

@app.get("/name")
def name():
    return {"Your Name"}

@api.get("/customer/{idx}")
def customer(idx: int):
    # read the data into a df
    df = pd.read_csv("../customers.csv")
    # filter the data based on the index
    customer =  df.iloc[idx]
    return customer.to_dict()