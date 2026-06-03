import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
import os

FEATURES = [
    "co2", "so2", "no2", "pm25", "pm10",
    "temperature", "humidity", "fuel_consumption",
    "operating_hours", "hour_of_day", "day_of_week"
]

def load_and_clean(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, parse_dates=["timestamp"])
    df.dropna(subset=FEATURES + ["aqi"], inplace=True)
    df["hour_of_day"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek
    df = df[(df["co2"] > 0) & (df["pm25"] >= 0)]
    return df

def scale_features(X_train, X_test, scaler_path="models/scaler.pkl"):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled  = scaler.transform(X_test)
    os.makedirs(os.path.dirname(scaler_path), exist_ok=True)
    joblib.dump(scaler, scaler_path)
    return X_train_scaled, X_test_scaled, scaler

def preprocess_realtime(data: dict, scaler_path="models/scaler.pkl") -> np.ndarray:
    import datetime
    now = datetime.datetime.now()
    row = {k: data.get(k, 0) for k in FEATURES[:9]}
    row["hour_of_day"] = now.hour
    row["day_of_week"] = now.weekday()
    df = pd.DataFrame([row])[FEATURES]
    scaler = joblib.load(scaler_path)
    return scaler.transform(df)
