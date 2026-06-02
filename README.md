<div align="center">

<!-- BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00C9FF,100:92FE9D&height=200&section=header&text=🌿%20AirGuard%20AI&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=AI-Powered%20Industrial%20Air%20Pollution%20Forecasting%20%26%20Monitoring%20System&descAlignY=55&descSize=18" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML%20Engine-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Twilio](https://img.shields.io/badge/Twilio-SMS%20Alerts-F22F46?style=for-the-badge&logo=twilio&logoColor=white)](https://twilio.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()

<br/>

> **🚨 Predicting industrial pollution BEFORE it becomes dangerous — protecting lives, communities, and the environment.**

<br/>

[🔍 Features](#-key-features) · [🏗️ Architecture](#️-system-architecture) · [🚦 Alert System](#-escalation-alert-system) · [📊 Dashboard](#-real-time-dashboard) · [🔐 Roles](#-role-based-access) · [⚡ Quick Start](#-quick-start) · [📁 Structure](#-project-structure)

</div>

---

## 🌍 The Problem We're Solving

<table>
<tr>
<td width="60%">

Every year, **millions of people** are harmed by industrial air pollution — but most monitoring systems only **detect** pollution *after* it has already become dangerous.

**AirGuard AI** flips this model entirely.

By analyzing real-time sensor data from factories and thermal power plants — including CO₂, SO₂, NO₂, PM2.5, PM10, temperature, humidity, fuel consumption, and operating hours — the system **forecasts dangerous emission events hours in advance** and automatically alerts the right people at the right time.

</td>
<td width="40%" align="center">

```
🏭  Factory Emitting Gases
        ↓
🤖  ML Model Predicts Danger
        ↓
📊  Dashboard Turns Red
        ↓
📱  SMS Alert Fires Instantly
        ↓
✅  Action Taken BEFORE Crisis
```

</td>
</tr>
</table>

---

## ✨ Key Features

<table>
<tr>
<td align="center" width="25%">
<h3>🔮</h3>
<b>AI Forecasting</b><br/>
<sub>Predicts future pollution levels using trained ML models on historical industrial data</sub>
</td>
<td align="center" width="25%">
<h3>📡</h3>
<b>Real-Time Monitoring</b><br/>
<sub>Live dashboard tracks CO₂, SO₂, NO₂, PM2.5, PM10, temperature & humidity</sub>
</td>
<td align="center" width="25%">
<h3>🚨</h3>
<b>Smart SMS Alerts</b><br/>
<sub>3-level escalation system via Twilio — from factory owner to government authority</sub>
</td>
<td align="center" width="25%">
<h3>🗺️</h3>
<b>Factory Map View</b><br/>
<sub>Color-coded status: 🟢 Safe · 🟡 Warning · 🔴 Dangerous</sub>
</td>
</tr>
<tr>
<td align="center" width="25%">
<h3>👥</h3>
<b>Role-Based Access</b><br/>
<sub>Separate dashboards for Admin, Factory Owner, Authority, and Worker</sub>
</td>
<td align="center" width="25%">
<h3>📈</h3>
<b>Trend Visualization</b><br/>
<sub>Time-series charts, pollution history, and predictive trend lines</sub>
</td>
<td align="center" width="25%">
<h3>⚙️</h3>
<b>Multi-Pollutant Analysis</b><br/>
<sub>Tracks 8+ environmental parameters simultaneously</sub>
</td>
<td align="center" width="25%">
<h3>🛡️</h3>
<b>Threshold Engine</b><br/>
<sub>Customizable safe/warning/danger thresholds per pollutant per factory</sub>
</td>
</tr>
</table>

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        AirGuard AI System                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   🏭 DATA SOURCES              🧠 ML ENGINE                        │
│   ┌──────────────┐             ┌──────────────────────────────┐     │
│   │ IoT Sensors  │──────────▶  │  Data Preprocessing          │     │
│   │ • CO₂        │             │  (Pandas + NumPy)            │     │
│   │ • SO₂        │             │         ↓                    │     │
│   │ • NO₂        │             │  Feature Engineering         │     │
│   │ • PM2.5      │             │         ↓                    │     │
│   │ • PM10       │             │  Scikit-learn Models         │     │
│   │ • Temp       │             │  (Random Forest / XGBoost)   │     │
│   │ • Humidity   │             │         ↓                    │     │
│   │ • Fuel Use   │             │  Pollution Forecast          │     │
│   └──────────────┘             └──────────┬───────────────────┘     │
│                                           │                         │
│   ⚡ FLASK BACKEND                        ▼                         │
│   ┌──────────────────────────────────────────────────────────┐      │
│   │  REST API  →  Threshold Check  →  Alert Engine           │      │
│   └────────────────────────┬─────────────────────────────────┘      │
│                            │                                        │
│         ┌──────────────────┼──────────────────┐                    │
│         ▼                  ▼                  ▼                     │
│   📊 Dashboard        📱 Twilio SMS      🗄️ Database               │
│   (Real-Time)         (Escalation)       (History)                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🚦 Escalation Alert System

> **The right person gets alerted at the right time — automatically.**

```
POLLUTION LEVEL RISING...
         │
         ▼
┌─────────────────────────────────────────────────────┐
│                                                     │
│  🟡  LEVEL 1  —  WARNING THRESHOLD CROSSED         │
│      ↳ 📱 SMS → Factory Owner                      │
│         "Pollution rising at Plant A. Take action." │
│                                                     │
│  🟠  LEVEL 2  —  DANGER THRESHOLD CROSSED          │
│      ↳ 📱 SMS → Safety Manager                     │
│         "URGENT: Unsafe levels at Plant A!          │
│          Immediate intervention required."          │
│                                                     │
│  🔴  LEVEL 3  —  CRITICAL / REGULATORY BREACH      │
│      ↳ 📱 SMS → Government Authority               │
│         "CRITICAL ALERT: Plant A exceeds legal      │
│          limits. Regulatory action may be needed."  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

| Level | Trigger | Recipient | Action Required |
|-------|---------|-----------|-----------------|
| 🟡 Level 1 | Approaches safe limit | Factory Owner | Monitor & adjust operations |
| 🟠 Level 2 | Exceeds safe threshold | Safety Manager | Reduce output / inspect systems |
| 🔴 Level 3 | Exceeds regulatory limit | Government Authority | Shutdown / legal action |

---

## 🗺️ Factory Status Map

Each factory on the monitoring map is color-coded in real time:

```
  🟢  GREEN  —  Safe
       All pollutant levels within safe environmental limits.
       No action required.

  🟡  YELLOW  —  Warning
       One or more pollutants approaching the safe threshold.
       Factory owner alerted. Monitoring increased.

  🔴  RED  —  Dangerous
       Pollutant levels exceed safe limits.
       Escalation chain triggered. Immediate action required.
```

This visual map is ideal for authorities monitoring multiple factories across a region simultaneously.

---

## 📊 Real-Time Dashboard

The monitoring dashboard provides:

- **Live pollution gauges** — animated dials for CO₂, SO₂, NO₂, PM2.5, PM10
- **Time-series trend charts** — historical + ML forecast overlay
- **Factory status cards** — color-coded with key metrics
- **Alert history log** — timestamped record of all SMS alerts sent
- **Environmental heatmap** — pollution intensity across monitored facilities

---

## 🔐 Role-Based Access

| Role | Access Level | Key Capabilities |
|------|-------------|-----------------|
| 🔴 **Admin** | Full system access | Manage users, configure thresholds, view all data |
| 🏭 **Factory Owner** | Own factory data | View live metrics, forecast, alert history |
| 🏛️ **Government Authority** | Read-only all factories | Regional overview, compliance status, escalation logs |
| 👷 **Worker** | Basic status view | Current safety status of their facility |

---

## 🧠 Machine Learning Pipeline

```python
# Simplified ML pipeline overview

# 1. Input Features
features = ['CO2', 'SO2', 'NO2', 'PM2_5', 'PM10',
            'temperature', 'humidity', 'fuel_consumption',
            'operating_hours', 'hour_of_day', 'day_of_week']

# 2. Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)

# 3. Model Training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_scaled, y_train)

# 4. Forecast Output
predicted_aqi = model.predict(X_future)

# 5. Alert Trigger
if predicted_aqi > DANGER_THRESHOLD:
    trigger_escalation(level=3)
```

**Monitored Pollutants & Parameters:**

| Parameter | Unit | Safe Limit | Warning | Danger |
|-----------|------|-----------|---------|--------|
| CO₂ | ppm | < 1000 | 1000–2000 | > 2000 |
| SO₂ | µg/m³ | < 80 | 80–200 | > 200 |
| NO₂ | µg/m³ | < 100 | 100–200 | > 200 |
| PM2.5 | µg/m³ | < 35 | 35–75 | > 75 |
| PM10 | µg/m³ | < 150 | 150–250 | > 250 |

---

## ⚡ Quick Start

### Prerequisites

```bash
Python 3.9+
pip
Twilio Account (for SMS alerts)
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/airguard-ai.git
cd airguard-ai

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env with your Twilio credentials and thresholds

# 5. Initialize the database
python scripts/init_db.py

# 6. Train the ML model
python scripts/train_model.py

# 7. Launch the application
python app.py
```

### Environment Configuration

```env
# .env.example

# Flask
FLASK_ENV=development
SECRET_KEY=your_secret_key_here

# Twilio SMS Alerts
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=+1234567890

# Alert Recipients
FACTORY_OWNER_PHONE=+91XXXXXXXXXX
SAFETY_MANAGER_PHONE=+91XXXXXXXXXX
GOVERNMENT_AUTHORITY_PHONE=+91XXXXXXXXXX

# Pollution Thresholds
CO2_WARNING=1000
CO2_DANGER=2000
PM25_WARNING=35
PM25_DANGER=75
```

---

## 📁 Project Structure

```
airguard-ai/
│
├── app.py                      # Flask application entry point
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variable template
│
├── models/                     # ML model files
│   ├── pollution_forecast.pkl  # Trained prediction model
│   └── scaler.pkl              # Feature scaler
│
├── ml/                         # Machine learning pipeline
│   ├── train_model.py          # Model training script
│   ├── predict.py              # Real-time prediction engine
│   └── preprocess.py           # Data preprocessing utilities
│
├── routes/                     # Flask route handlers
│   ├── auth.py                 # Login / role-based access
│   ├── dashboard.py            # Dashboard routes
│   ├── api.py                  # REST API endpoints
│   └── alerts.py               # Alert management
│
├── alerts/                     # Twilio SMS alert system
│   ├── twilio_client.py        # Twilio API integration
│   └── escalation.py           # 3-level escalation logic
│
├── templates/                  # HTML templates
│   ├── admin/                  # Admin dashboard views
│   ├── factory_owner/          # Factory owner views
│   ├── authority/              # Government authority views
│   └── worker/                 # Worker views
│
├── static/                     # CSS, JS, assets
│   ├── css/
│   ├── js/
│   └── charts/
│
├── data/                       # Sample datasets
│   ├── industrial_data.csv
│   └── historical_emissions.csv
│
└── scripts/                    # Utility scripts
    ├── init_db.py              # Database initialization
    └── simulate_sensors.py     # Sensor data simulator for testing
```

---

## 🛠️ Tech Stack

<table>
<tr>
<th>Layer</th>
<th>Technology</th>
<th>Purpose</th>
</tr>
<tr>
<td>Backend</td>
<td>Python + Flask</td>
<td>REST API, routing, business logic</td>
</tr>
<tr>
<td>ML / Data</td>
<td>Scikit-learn, Pandas, NumPy</td>
<td>Forecasting, preprocessing, analysis</td>
</tr>
<tr>
<td>Alerts</td>
<td>Twilio API</td>
<td>Automated SMS escalation system</td>
</tr>
<tr>
<td>Frontend</td>
<td>HTML, CSS, JavaScript, Chart.js</td>
<td>Real-time dashboard & visualizations</td>
</tr>
<tr>
<td>Database</td>
<td>SQLite / PostgreSQL</td>
<td>Sensor data, user management, alert logs</td>
</tr>
<tr>
<td>Auth</td>
<td>Flask-Login + JWT</td>
<td>Role-based access control</td>
</tr>
</table>

---

## 📈 Impact & Applications

- **🏭 Industrial Compliance** — Helps factories stay within legal emission limits proactively
- **🏥 Public Health** — Early warnings reduce community exposure to hazardous gases
- **🌿 Environmental Protection** — Enables faster regulatory response to pollution events
- **📋 Data-Driven Policy** — Historical trends support evidence-based environmental regulation
- **🤝 Government Integration** — Provides authorities real-time visibility across all monitored facilities

---

## 🔮 Future Enhancements

- [ ] Mobile app (Android/iOS) for on-the-go monitoring
- [ ] Integration with national air quality APIs (CPCB, EPA)
- [ ] Drone-based sensor data ingestion
- [ ] LSTM deep learning model for improved time-series forecasting
- [ ] Satellite imagery integration for regional pollution mapping
- [ ] WhatsApp alerts in addition to SMS

---

## 👨‍💻 Author

<div align="center">

**Developed with ❤️ to protect communities and the environment**

*This project demonstrates the real-world application of AI, Machine Learning, and real-time communication technologies to solve critical industrial pollution challenges.*

---

⭐ **Star this repo if you find it useful!** ⭐

</div>

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:92FE9D,100:00C9FF&height=100&section=footer" width="100%"/>
</div>
