import os
from alerts.twilio_client import send_sms
from database import db, AlertLog
from datetime import datetime

THRESHOLDS = {
    "co2" : {"warning": float(os.getenv("CO2_WARNING",  1000)),
              "danger" : float(os.getenv("CO2_DANGER",   2000))},
    "so2" : {"warning": float(os.getenv("SO2_WARNING",    80)),
              "danger" : float(os.getenv("SO2_DANGER",    200))},
    "no2" : {"warning": float(os.getenv("NO2_WARNING",   100)),
              "danger" : float(os.getenv("NO2_DANGER",    200))},
    "pm25": {"warning": float(os.getenv("PM25_WARNING",   35)),
              "danger" : float(os.getenv("PM25_DANGER",    75))},
    "pm10": {"warning": float(os.getenv("PM10_WARNING",  150)),
              "danger" : float(os.getenv("PM10_DANGER",   250))},
}

MESSAGES = {
    1: ("WARNING",  "⚠️ AirGuard LEVEL 1 WARNING: {pollutant} at {factory} has reached {value} {unit} "
                    "(safe limit: {limit}). Please take preventive action now."),
    2: ("DANGER",   "🚨 AirGuard LEVEL 2 DANGER: {pollutant} at {factory} is {value} {unit} — "
                    "exceeding safe limits. IMMEDIATE intervention required."),
    3: ("CRITICAL", "🔴 AirGuard LEVEL 3 CRITICAL: {factory} is breaching regulatory emission limits "
                    "({pollutant}: {value} {unit}). Government regulatory action may be required."),
}

UNITS = {"co2": "ppm", "so2": "µg/m³", "no2": "µg/m³", "pm25": "µg/m³", "pm10": "µg/m³"}

def check_and_escalate(factory, reading, owner_phone, manager_phone, authority_phone):
    """
    Check all pollutants against thresholds and fire escalation SMS as needed.
    factory        : Factory ORM object
    reading        : SensorReading ORM object (just saved)
    *_phone        : recipient phone numbers
    """
    contacts = {
        1: ("Factory Owner",       owner_phone),
        2: ("Safety Manager",      manager_phone),
        3: ("Government Authority", authority_phone),
    }

    pollutant_values = {
        "co2" : reading.co2,
        "so2" : reading.so2,
        "no2" : reading.no2,
        "pm25": reading.pm25,
        "pm10": reading.pm10,
    }

    triggered_level = 0

    for pollutant, value in pollutant_values.items():
        if value is None:
            continue
        limits = THRESHOLDS[pollutant]

        if value >= limits["danger"]:
            level     = 3
            threshold = limits["danger"]
        elif value >= limits["warning"]:
            level     = 2
            threshold = limits["warning"]
        elif value >= limits["warning"] * 0.8:
            level     = 1
            threshold = limits["warning"]
        else:
            continue

        if level <= triggered_level:
            continue
        triggered_level = level

        recipient_name, phone = contacts[level]
        _, template = MESSAGES[level]
        body = template.format(
            pollutant=pollutant.upper(),
            factory=factory.name,
            value=round(value, 1),
            unit=UNITS[pollutant],
            limit=threshold,
        )

        result = send_sms(phone, body)

        log = AlertLog(
            factory_id=factory.id,
            level=level,
            pollutant=pollutant,
            value=value,
            threshold=threshold,
            recipient=recipient_name,
            phone=phone,
            sms_status=result.get("status", "unknown"),
            timestamp=datetime.utcnow(),
        )
        db.session.add(log)

    db.session.commit()
    return triggered_level
