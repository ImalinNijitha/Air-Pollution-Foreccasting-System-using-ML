"""
Train the AirGuard AI pollution forecasting model.
Run:  python ml/train_model.py
"""
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from preprocess import load_and_clean, scale_features, FEATURES

DATA_PATH  = "data/industrial_data.csv"
MODEL_PATH = "models/pollution_forecast.pkl"

def train():
    print("[AirGuard] Loading data...")
    df = load_and_clean(DATA_PATH)
    X  = df[FEATURES]
    y  = df["aqi"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    X_train_s, X_test_s, _ = scale_features(X_train, X_test)

    print("[AirGuard] Training Random Forest model...")
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=15,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train_s, y_train)

    preds = model.predict(X_test_s)
    print(f"[AirGuard] MAE  : {mean_absolute_error(y_test, preds):.2f}")
    print(f"[AirGuard] R²   : {r2_score(y_test, preds):.4f}")

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"[AirGuard] Model saved → {MODEL_PATH}")

if __name__ == "__main__":
    train()
