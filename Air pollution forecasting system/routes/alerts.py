from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from database import AlertLog, Factory

alerts_bp = Blueprint("alerts", __name__)

@alerts_bp.route("/")
@login_required
def alert_history():
    if current_user.role == "authority":
        logs = (AlertLog.query
                .filter(AlertLog.level >= 3)
                .order_by(AlertLog.timestamp.desc())
                .limit(100).all())
    elif current_user.role in ("admin",):
        logs = AlertLog.query.order_by(AlertLog.timestamp.desc()).limit(100).all()
    else:
        logs = (AlertLog.query
                .filter_by(factory_id=current_user.factory_id)
                .order_by(AlertLog.timestamp.desc())
                .limit(50).all())
    return render_template("alerts/history.html", logs=logs)

@alerts_bp.route("/test-sms/<int:level>")
@login_required
def test_sms(level):
    """Admin-only: fire a test SMS at the given escalation level."""
    if current_user.role != "admin":
        return jsonify({"error": "Unauthorized"}), 403
    from alerts.twilio_client import send_sms
    import os
    phones = {
        1: os.getenv("FACTORY_OWNER_PHONE"),
        2: os.getenv("SAFETY_MANAGER_PHONE"),
        3: os.getenv("GOVERNMENT_AUTHORITY_PHONE"),
    }
    phone = phones.get(level)
    if not phone:
        return jsonify({"error": f"No phone configured for level {level}"}), 400
    result = send_sms(phone, f"[AirGuard TEST] Level {level} alert system check. Ignore this message.")
    return jsonify(result)
