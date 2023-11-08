import pickle
from pathlib import Path

__version__ = "0.1.1"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/regression_pipeline-{__version__}.pkl","rb") as f:
    model = pickle.load(f)

def predict_pipeline(health_stats):
    # check if they are float
    # check if they have categorical values
    # check the order of the parameters
    
    pred = model.predict([health_stats])
    return pred[0]