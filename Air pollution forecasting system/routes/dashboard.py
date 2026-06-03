from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from database import Factory, SensorReading, AlertLog

dashboard_bp = Blueprint("dashboard", __name__)

ROLE_TEMPLATE = {
    "admin"         : "admin/dashboard.html",
    "factory_owner" : "factory_owner/dashboard.html",
    "authority"     : "authority/dashboard.html",
    "worker"        : "worker/dashboard.html",
}

@dashboard_bp.route("/")
@login_required
def home():
    template = ROLE_TEMPLATE.get(current_user.role, "worker/dashboard.html")

    if current_user.role == "admin":
        factories = Factory.query.all()
        alerts    = AlertLog.query.order_by(AlertLog.timestamp.desc()).limit(20).all()
        return render_template(template, factories=factories, alerts=alerts)

    if current_user.role == "factory_owner":
        factory  = Factory.query.get(current_user.factory_id)
        readings = (SensorReading.query
                    .filter_by(factory_id=factory.id)
                    .order_by(SensorReading.timestamp.desc())
                    .limit(50).all())
        alerts   = (AlertLog.query
                    .filter_by(factory_id=factory.id)
                    .order_by(AlertLog.timestamp.desc())
                    .limit(10).all())
        return render_template(template, factory=factory, readings=readings, alerts=alerts)

    if current_user.role == "authority":
        factories = Factory.query.all()
        alerts    = (AlertLog.query
                     .filter(AlertLog.level >= 3)
                     .order_by(AlertLog.timestamp.desc())
                     .limit(30).all())
        return render_template(template, factories=factories, alerts=alerts)

    # worker
    factory = Factory.query.get(current_user.factory_id)
    latest  = (SensorReading.query
               .filter_by(factory_id=factory.id)
               .order_by(SensorReading.timestamp.desc())
               .first())
    return render_template(template, factory=factory, latest=latest)
