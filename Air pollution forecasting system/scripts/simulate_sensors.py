"""
Simulate continuous sensor data for all factories.
Sends POST requests to the /api/readings endpoint.
Run:  python scripts/simulate_sensors.py
"""
import sys, os, time, random, requests
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

BASE_URL   = "http://localhost:5000"
FACTORY_IDS = [1, 2, 3, 4, 5, 6]
INTERVAL   = 10  # seconds between readings

def simulate_reading(factory_id: int) -> dict:
    """Generate realistic sensor readings with occasional spikes."""
    spike = random.random() < 0.1  # 10% chance of a spike

    return {
        "factory_id"      : factory_id,
        "co2"             : round(random.uniform(400, 2500 if spike else 900), 1),
        "so2"             : round(random.uniform(10,  250  if spike else 90),  1),
        "no2"             : round(random.uniform(10,  220  if spike else 95),  1),
        "pm25"            : round(random.uniform(5,   90   if spike else 40),  1),
        "pm10"            : round(random.uniform(20,  280  if spike else 140), 1),
        "temperature"     : round(random.uniform(22,  48),  1),
        "humidity"        : round(random.uniform(30,  90),  1),
        "fuel_consumption": round(random.uniform(50,  500), 1),
        "operating_hours" : round(random.uniform(0,   24),  1),
        "aqi"             : round(random.uniform(20,  250 if spike else 80),   1),
    }

def main():
    print(f"[AirGuard Simulator] Starting — posting every {INTERVAL}s to {BASE_URL}")
    while True:
        for fid in FACTORY_IDS:
            payload = simulate_reading(fid)
            try:
                r = requests.post(f"{BASE_URL}/api/readings", json=payload, timeout=5)
                status = r.json()
                print(f"  Factory {fid} → AQI {payload['aqi']:6.1f}  "
                      f"alert_level={status.get('alert_level', 0)}  "
                      f"status={status.get('forecast', {}).get('status', '?')}")
            except Exception as e:
                print(f"  Factory {fid} → ERROR: {e}")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
