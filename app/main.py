from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from .model.model import predict_pipeline
from .model.model import __version__ as model_version

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HealthStats(BaseModel):
	Gender:int
	Age:float
	Height:float
	Weight:float
	Duration:float
	Heart_Rate:float
	Body_Temp:float

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict")
def predict(payload: HealthStats):
    health_stats = [payload.Gender,payload.Age,payload.Height,payload.Weight,payload.Duration,payload.Heart_Rate,payload.Body_Temp]
    return {"burned calories": predict_pipeline(health_stats=health_stats)}



