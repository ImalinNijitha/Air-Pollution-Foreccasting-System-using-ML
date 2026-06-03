from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from database import db, Factory, SensorReading, AlertLog
from ml.predict import get_pollutant_forecast, classify_status
from alerts.escalation import check_and_escalate
import os

api_bp = Blueprint("api", __name__)

@api_bp.route("/readings", methods=["POST"])
def ingest_reading():
    """Receive sensor data, run forecast, trigger alerts if needed."""
    data       = request.json
    factory_id = data.get("factory_id")
    factory    = Factory.query.get_or_404(factory_id)

    reading = SensorReading(
        factory_id      = factory_id,
        co2             = data.get("co2"),
        so2             = data.get("so2"),
        no2             = data.get("no2"),
        pm25            = data.get("pm25"),
        pm10            = data.get("pm10"),
        temperature     = data.get("temperature"),
        humidity        = data.get("humidity"),
        fuel_consumption= data.get("fuel_consumption"),
        operating_hours = data.get("operating_hours"),
        aqi             = data.get("aqi"),
    )
    db.session.add(reading)

    forecast = get_pollutant_forecast(data)
    factory.status = forecast["status"]
    db.session.commit()

    level = check_and_escalate(
        factory   = factory,
        reading   = reading,
        owner_phone     = os.getenv("FACTORY_OWNER_PHONE", ""),
        manager_phone   = os.getenv("SAFETY_MANAGER_PHONE", ""),
        authority_phone = os.getenv("GOVERNMENT_AUTHORITY_PHONE", ""),
    )

    return jsonify({
        "status"   : "ok",
        "forecast" : forecast,
        "alert_level": level,
    }), 201

@api_bp.route("/factories", methods=["GET"])
@login_required
def get_factories():
    factories = Factory.query.all()
    return jsonify([{
        "id"      : f.id,
        "name"    : f.name,
        "type"    : f.type,
        "location": f.location,
        "lat"     : f.lat,
        "lng"     : f.lng,
        "status"  : f.status,
    } for f in factories])

@api_bp.route("/factories/<int:fid>/readings", methods=["GET"])
@login_required
def factory_readings(fid):
    readings = (SensorReading.query
                .filter_by(factory_id=fid)
                .order_by(SensorReading.timestamp.desc())
                .limit(100).all())
    return jsonify([{
        "timestamp"  : r.timestamp.isoformat(),
        "co2"        : r.co2,
        "so2"        : r.so2,
        "no2"        : r.no2,
        "pm25"       : r.pm25,
        "pm10"       : r.pm10,
        "temperature": r.temperature,
        "humidity"   : r.humidity,
        "aqi"        : r.aqi,
    } for r in readings])

@api_bp.route("/alerts", methods=["GET"])
@login_required
def get_alerts():
    level = request.args.get("level", type=int)
    q = AlertLog.query
    if level:
        q = q.filter(AlertLog.level == level)
    logs = q.order_by(AlertLog.timestamp.desc()).limit(50).all()
    return jsonify([{
        "id"        : a.id,
        "factory_id": a.factory_id,
        "level"     : a.level,
        "pollutant" : a.pollutant,
        "value"     : a.value,
        "threshold" : a.threshold,
        "recipient" : a.recipient,
        "sms_status": a.sms_status,
        "timestamp" : a.timestamp.isoformat(),
    } for a in logs])

@api_bp.route("/forecast", methods=["POST"])
def forecast():
    data = request.json
    try:
        result = get_pollutant_forecast(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
