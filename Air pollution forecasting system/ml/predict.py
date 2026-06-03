import joblib
import numpy as np
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from preprocess import preprocess_realtime

MODEL_PATH  = "models/pollution_forecast.pkl"
SCALER_PATH = "models/scaler.pkl"

_model  = None

def _load():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)

def predict_aqi(sensor_data: dict) -> float:
    """Return predicted AQI for a dict of sensor readings."""
    _load()
    X = preprocess_realtime(sensor_data, SCALER_PATH)
    return float(np.round(_model.predict(X)[0], 2))

def classify_status(aqi: float) -> str:
    if aqi < 50:
        return "green"
    if aqi < 100:
        return "yellow"
    return "red"

def get_pollutant_forecast(sensor_data: dict) -> dict:
    """Return per-pollutant predicted next-hour values."""
    aqi    = predict_aqi(sensor_data)
    factor = 1 + (aqi - 50) / 500
    return {
        "predicted_aqi" : aqi,
        "status"        : classify_status(aqi),
        "co2_forecast"  : round(sensor_data.get("co2",  0) * factor, 1),
        "so2_forecast"  : round(sensor_data.get("so2",  0) * factor, 1),
        "no2_forecast"  : round(sensor_data.get("no2",  0) * factor, 1),
        "pm25_forecast" : round(sensor_data.get("pm25", 0) * factor, 1),
        "pm10_forecast" : round(sensor_data.get("pm10", 0) * factor, 1),
    }
