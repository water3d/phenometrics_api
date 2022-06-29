import sys
from fastapi import FastAPI
from pydantic import BaseModel

sys.path.insert(0, r"C:\Users\dsx\CodeLocal\phenometrics_api")

from phenometrics import timeseries


class Measurement(BaseModel):
	index_value: float
	date: str
	timestamp: float | None = None


app = FastAPI()


@app.get("/")
async def root():
	return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
	return {"message": f"Hello {name}"}


@app.post("/phenometrics/simple/")
async def phenology_simple(measurements: list[Measurement]):
	measurements_dict = [{"index_value": m.index_value, "date": m.date, "timestamp": m.timestamp} for m in measurements]
	results = timeseries.get_phenometrics_basic(measurements_dict, index_field="index_value", date_field="date")

	return str([{val: getattr(results, val) for val in results.keys()}])