from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id         = db.Column(db.Integer, primary_key=True)
    username   = db.Column(db.String(80), unique=True, nullable=False)
    email      = db.Column(db.String(120), unique=True, nullable=False)
    password   = db.Column(db.String(200), nullable=False)
    role       = db.Column(db.String(20), nullable=False)   # admin|factory_owner|authority|worker
    factory_id = db.Column(db.Integer, db.ForeignKey("factories.id"), nullable=True)
    phone      = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Factory(db.Model):
    __tablename__ = "factories"
    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(120), nullable=False)
    type     = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    lat      = db.Column(db.Float, nullable=True)
    lng      = db.Column(db.Float, nullable=True)
    status   = db.Column(db.String(10), default="green")  # green|yellow|red
    users    = db.relationship("User", backref="factory", lazy=True)
    readings = db.relationship("SensorReading", backref="factory", lazy=True)

class SensorReading(db.Model):
    __tablename__ = "sensor_readings"
    id              = db.Column(db.Integer, primary_key=True)
    factory_id      = db.Column(db.Integer, db.ForeignKey("factories.id"), nullable=False)
    timestamp       = db.Column(db.DateTime, default=datetime.utcnow)
    co2             = db.Column(db.Float)
    so2             = db.Column(db.Float)
    no2             = db.Column(db.Float)
    pm25            = db.Column(db.Float)
    pm10            = db.Column(db.Float)
    temperature     = db.Column(db.Float)
    humidity        = db.Column(db.Float)
    fuel_consumption= db.Column(db.Float)
    operating_hours = db.Column(db.Float)
    aqi             = db.Column(db.Float)

class AlertLog(db.Model):
    __tablename__ = "alert_logs"
    id         = db.Column(db.Integer, primary_key=True)
    factory_id = db.Column(db.Integer, db.ForeignKey("factories.id"), nullable=False)
    level      = db.Column(db.Integer, nullable=False)   # 1, 2, or 3
    pollutant  = db.Column(db.String(20))
    value      = db.Column(db.Float)
    threshold  = db.Column(db.Float)
    recipient  = db.Column(db.String(120))
    phone      = db.Column(db.String(20))
    sms_status = db.Column(db.String(20))
    timestamp  = db.Column(db.DateTime, default=datetime.utcnow)
