"""
Generate sample industrial_data.csv for model training.
Run:  python data/generate_sample_data.py
"""
import pandas as pd
import numpy as np
import os

np.random.seed(42)
N = 5000

timestamps = pd.date_range("2023-01-01", periods=N, freq="30min")

co2  = np.random.uniform(400,  2000, N)
so2  = np.random.uniform(10,   220,  N)
no2  = np.random.uniform(10,   210,  N)
pm25 = np.random.uniform(5,    90,   N)
pm10 = np.random.uniform(20,   280,  N)
temp = np.random.uniform(20,   50,   N)
hum  = np.random.uniform(30,   90,   N)
fuel = np.random.uniform(50,   500,  N)
hrs  = np.random.uniform(0,    24,   N)

# AQI is a weighted composite (simplified)
aqi = (
    0.25 * (pm25 / 90  * 200) +
    0.20 * (pm10 / 280 * 200) +
    0.20 * (so2  / 220 * 200) +
    0.20 * (no2  / 210 * 200) +
    0.15 * (co2  / 2000* 200)
)

df = pd.DataFrame({
    "timestamp"       : timestamps,
    "co2"             : np.round(co2,  1),
    "so2"             : np.round(so2,  1),
    "no2"             : np.round(no2,  1),
    "pm25"            : np.round(pm25, 1),
    "pm10"            : np.round(pm10, 1),
    "temperature"     : np.round(temp, 1),
    "humidity"        : np.round(hum,  1),
    "fuel_consumption": np.round(fuel, 1),
    "operating_hours" : np.round(hrs,  1),
    "aqi"             : np.round(aqi,  1),
})

out = os.path.join(os.path.dirname(__file__), "industrial_data.csv")
df.to_csv(out, index=False)
print(f"[AirGuard] Generated {N} sample readings → {out}")
