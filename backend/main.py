from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
from .calc import compute_daily

app = FastAPI(title="Time Clock API")

class Shift(BaseModel):
    in_ts: datetime
    out_ts: datetime
    breaks: float = 0.0  # breaks in minutes


@app.post("/calc/day")
def calc_day(shift: Shift):
    net_break = timedelta(minutes=shift.breaks)
    result = compute_daily(shift.in_ts, shift.out_ts, net_break)
    return result
