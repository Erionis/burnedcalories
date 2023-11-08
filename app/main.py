
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # 

from pydantic import BaseModel

from .model.model import predict_pipeline
from .model.model import __version__ as model_version

app = FastAPI()
origins = [
    "*"  # allow everybody to send request
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create a class where the inner parameters are the features
class HealthStats(BaseModel):
	Gender:int
	Age:float
	Height:float
	Weight:float
	Duration:float
	Heart_Rate:float
	Body_Temp:float

# our request can be a GET and POST
# HTTP GET they want to read some data
@app.get("/")  # create a ENDPOINT to the root of the server
def home(): # this function will be activated
    return {"health_check": "OK", "model_version": model_version}
# HTTP POST, they are sending data to me
@app.post("/predict")  # ENDPOINT
def predict(payload: HealthStats): # this function will be activated
    health_stats = [payload.Gender,payload.Age,payload.Height,payload.Weight,payload.Duration,payload.Heart_Rate,payload.Body_Temp]
    return {"burned calories": predict_pipeline(health_stats=health_stats)}



