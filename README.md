<div align="center">

<br/>
"AIR POLLUTION FORECASTING SYSTEM USING ML"


[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=3000&pause=1000&color=00FF88&center=true&vCenter=true&multiline=true&width=700&height=60&lines=Predicting+pollution+BEFORE+it+becomes+dangerous+🚨;Protecting+workers%2C+communities+%26+the+environment+🌿)](https://git.io/typing-svg)

<br/>

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML%20Engine-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Twilio](https://img.shields.io/badge/Twilio-SMS%20Alerts-F22F46?style=for-the-badge&logo=twilio&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Scientific-013243?style=for-the-badge&logo=numpy&logoColor=white)

<br/>

![Status](https://img.shields.io/badge/Status-Active%20Development-00ff88?style=flat-square)
![Tamil Nadu](https://img.shields.io/badge/Built%20in-Tamil%20Nadu%2C%20India-FF9933?style=flat-square)

</div>

---

## 🌍 The Problem

> Every year, **millions of people** are harmed by industrial air pollution — but most systems only detect it *after* it is already dangerous.

This model analyzes real-time sensor data from factories and thermal power plants, the system **forecasts dangerous emission events in advance** and automatically alerts the right people at the right time — before harm is done.

---

## ⚡ Live Sensor Simulation Demo

```
┌──────────────────────────────────────────────────────────────────────┐
│                     🛰  LIVE SENSOR DASHBOARD                        │
├────────────┬────────────┬────────────┬────────────┬──────────────────┤
│    CO₂     │    SO₂     │   PM2.5    │    NO₂     │      PM10        │
│   842 ppm  │ 124 µg/m³  │  78 µg/m³  │  67 µg/m³  │   183 µg/m³     │
│  🟢 SAFE   │ 🟡 WARNING │ 🔴 DANGER  │  🟢 SAFE   │  🟡 WARNING     │
└────────────┴────────────┴────────────┴────────────┴──────────────────┘
```

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔮 **AI Forecasting** | Predicts future pollution levels using trained ML models on industrial data |
| 📡 **Real-Time Monitoring** | Live dashboard tracks CO₂, SO₂, NO₂, PM2.5, PM10, temperature and humidity |
| 🚨 **3-Level SMS Alerts** | Automated escalation via Twilio — Factory Owner → Safety Manager → Government |
| 🗺️ **Factory Map** | Color-coded status map: 🟢 Safe · 🟡 Warning · 🔴 Dangerous |
| 👥 **Role-Based Login** | Separate dashboards for Admin, Factory Owner, Government Authority, Worker |
| 📈 **Trend Visualization** | Historical charts with ML forecast overlay in real time |
| ⚙️ **Multi-Pollutant** | Tracks 8+ environmental parameters simultaneously |
| 🛡️ **Threshold Engine** | Customizable safe/warning/danger limits per pollutant per factory |

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│                           AirGuard AI System                             │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   🏭 DATA SOURCES                     🧠 ML ENGINE                      │
│   ┌──────────────────┐                ┌────────────────────────────┐     │
│   │  IoT Sensors     │───────────────▶│  Preprocessing             │    │
│   │  • CO₂  • SO₂   │                 │  (Pandas + NumPy)          │     │
│   │  • NO₂  • PM2.5 │                 │          ↓                 │     │
│   │  • PM10 • Temp  │                 │  Feature Engineering       │     │
│   │  • Humidity     │                 │          ↓                 │     │
│   │  • Fuel Usage   │                 │  Scikit-learn Model        │     │
│   │  • Op. Hours    │                 │  (Random Forest)           │     │
│   └──────────────────┘                │          ↓                 │     │
│                                       │  Pollution Forecast        │     │
│                                       └────────────┬───────────────┘     │
│                                                    │                     │
│   ⚡ FLASK BACKEND                                 ▼                     │
│   ┌──────────────────────────────────────────────────────────────┐       │
│   │   REST API  ──▶  Threshold Check  ──▶  Alert Engine          │      │
│   └────────────────────────┬─────────────────────────────────────┘       │
│                            │                                             │
│          ┌─────────────────┼──────────────────┐                          │
│          ▼                 ▼                  ▼                          │
│    📊 Dashboard       📱 Twilio SMS      🗄️ Database                    |
│    (Real-Time)        (Escalation)       (History + Logs)                │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 🗺️ Factory Status Map

Each monitored factory is color-coded in real time:

```
  🟢  GREEN  ──  Safe
       All pollutants within environmental limits.
       No action required.

  🟡  YELLOW  ──  Warning
       One or more pollutants approaching safe threshold.
       Factory owner alerted. Monitoring intensified.

  🔴  RED  ──  Dangerous
       Pollutant levels exceed safe limits.
       Full escalation chain triggered. Immediate action required.
```

**Sample Factory Status:**

| Factory | Type | AQI | Status |
|---------|------|-----|--------|
| Coimbatore Plant A | Textile Manufacturing | 42 | 🟢 Safe |
| Chennai Thermal PP | Thermal Power Plant | 118 | 🟡 Warning |
| Salem Steel Works | Steel and Iron Industry | 214 | 🔴 Dangerous |
| Tirupur Dyeing Unit | Chemical Processing | 55 | 🟢 Safe |
| Erode Cement Works | Cement Production | 97 | 🟡 Warning |
| Madurai Refinery | Petroleum Refinery | 38 | 🟢 Safe |

---

## 🚨 Escalation Alert System

> The right person gets alerted at the right time — automatically.

```
POLLUTION LEVEL RISING...
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  🟡  LEVEL 1  ──  WARNING THRESHOLD CROSSED                │
│      Trigger  : Pollutant reaches 80% of safe limit         │
│      Action   : 📱 SMS ──▶ Factory Owner                   │
│      Message  : "Pollution rising at Plant A.               │
│                  Take preventive action now."               │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🟠  LEVEL 2  ──  DANGER THRESHOLD CROSSED                 │
│      Trigger  : Pollutant exceeds safe limit                │
│      Action   : 📱 SMS ──▶ Safety Manager                  │
│      Message  : "URGENT: Unsafe emission levels at          │
│                  Plant A. Immediate intervention needed."   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🔴  LEVEL 3  ──  REGULATORY BREACH                        │
│      Trigger  : Pollutant exceeds legal or regulatory limit │
│      Action   : 📱 SMS ──▶ Government Authority            │
│      Message  : "CRITICAL: Plant A exceeds legal emission   │
│                  limits. Regulatory action required."       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Level | Threshold | Recipient | Response |
|-------|-----------|-----------|----------|
| 🟡 Level 1 | 80% of safe limit | Factory Owner | Monitor and adjust operations |
| 🟠 Level 2 | Exceeds safe limit | Safety Manager | Reduce output, inspect systems |
| 🔴 Level 3 | Exceeds legal limit | Government Authority | Shutdown or regulatory action |

---

## 🧠 Machine Learning Pipeline

```
📡 Sensor Input        🧹 Preprocessing       🤖 ML Model
┌──────────────┐       ┌──────────────┐       ┌─────────────────┐
│ CO₂, SO₂     │──────▶│ Pandas clean │──────▶│ Random Forest   │
│ NO₂, PM2.5   │       │ NumPy scale  │       │ Feature import. │
│ PM10, Temp   │       │ Encode time  │       │ Cross-validate  │
│ Humidity     │       │ Handle nulls │       │ Fit & save .pkl │
│ Fuel, Hours  │       └──────────────┘       └────────┬────────┘
└──────────────┘                                       │
                                                       ▼
                                             🔮 Forecast Output
                                             ┌──────────────────┐
                                             │ Predicted AQI    │
                                             │ per pollutant    │
                                             │ for next N hours │
                                             └────────┬─────────┘
                                                      │
                                                      ▼
                                             ⚡ Threshold Check
                                             ┌──────────────────┐
                                             │ Safe?   → Monitor│
                                             │ Warn?   → Level 1│
                                             │ Danger? → L2/L3  │
                                             └──────────────────┘
```

**Pollutant Thresholds:**

| Parameter | Unit | 🟢 Safe | 🟡 Warning | 🔴 Danger |
|-----------|------|---------|-----------|----------|
| CO₂ | ppm | < 1000 | 1000–2000 | > 2000 |
| SO₂ | µg/m³ | < 80 | 80–200 | > 200 |
| NO₂ | µg/m³ | < 100 | 100–200 | > 200 |
| PM2.5 | µg/m³ | < 35 | 35–75 | > 75 |
| PM10 | µg/m³ | < 150 | 150–250 | > 250 |

---

## 🔐 Role-Based Access

```
┌────────────────┬────────────────────────────────────────────────────┐
│     Role       │  Capabilities                                      │
├────────────────┼────────────────────────────────────────────────────┤
│ 🔴 Admin       │ Manage users and factories, configure thresholds,  │
│                │ view all system data, access all escalation logs   │
├────────────────┼────────────────────────────────────────────────────┤
│ 🏭 Factory     │ Live emissions dashboard for own plant,            │
│    Owner       │ pollution forecasts, alert history, compliance     │
├────────────────┼────────────────────────────────────────────────────┤
│ 🏛️ Government  │ Regional all-factory overview map,                 │
│    Authority   │ regulatory breach history, Level 3 alert logs      │
├────────────────┼────────────────────────────────────────────────────┤
│ 👷 Worker      │ Current facility safety status, active alerts,     │
│                │ evacuation guidance when danger level reached      │
└────────────────┴────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

<div align="center">

![Skills](https://skillicons.dev/icons?i=python,flask,sklearn,html,css,js,sqlite,git&theme=dark)

</div>

| Layer | Technology | Purpose |
|-------|-----------|---------|
| 🐍 Backend | Python + Flask | REST API, routing, business logic |
| 🤖 ML / Data | Scikit-learn, Pandas, NumPy | Forecasting, preprocessing, analysis |
| 📱 Alerts | Twilio API | Automated 3-level SMS escalation |
| 📊 Frontend | HTML, CSS, JS, Chart.js | Real-time dashboard and visualizations |
| 🗄️ Database | SQLite / PostgreSQL | Sensor data, users, alert logs |
| 🔐 Auth | Flask-Login + JWT | Role-based access control |

---

### Environment Setup

```env
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

# Thresholds (customizable per factory)
CO2_WARNING=1000
CO2_DANGER=2000
PM25_WARNING=35
PM25_DANGER=75
SO2_WARNING=80
SO2_DANGER=200
```

---

## 📈 Impact

- 🏭 **Industrial Compliance** — Helps factories proactively stay within legal emission limits
- 🏥 **Public Health** — Early warnings reduce community exposure to hazardous gases
- 🌿 **Environmental Safety** — Faster response to pollution events before they escalate
- 📋 **Data-Driven Policy** — Historical trends support evidence-based environmental regulation
- 🤝 **Government Integration** — Real-time visibility across all monitored facilities

---

## 🔮 Future Roadmap

- [ ] 📱 Mobile app (Android / iOS) for on-the-go monitoring
- [ ] 🌐 Integration with national air quality APIs (CPCB, EPA)
- [ ] 🚁 Drone-based sensor data ingestion
- [ ] 🧠 LSTM deep learning model for improved time-series forecasting
- [ ] 🛰️ Satellite imagery for regional pollution heatmaps
- [ ] 💬 WhatsApp and Email alerts in addition to SMS
- [ ] 🌍 Multi-language support (Tamil, Hindi, English)

---

<div align="center">

### Developed by Imalin Nijitha 


<br/>

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00aaff,100:00ff88&height=120&section=footer" width="100%"/>

</div>
