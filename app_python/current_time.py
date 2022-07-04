from typing import Union

from fastapi import FastAPI

from datetime import datetime
import pytz

app = FastAPI()

def get_current_time():
    timeZ_Moscow = pytz.timezone('Europe/Moscow')
    dt_Moscow = datetime.now(timeZ_Moscow)
    return dt_Moscow.strftime('%Y-%m-%d %H:%M:%S %Z %z')


@app.get("/")
def read_root():
    # writing to file when root endpoint is hit
    with open('out.txt', 'w') as f:
       print( get_current_time(), file=f)  
    return "output redirected to a file..."

@app.get("/visit")
def read_root():
    return "--Current time in Moscow---" + get_current_time()
