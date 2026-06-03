"""
Initialize the database and seed sample factories and an admin user.
Run:  python scripts/init_db.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app
from database import db, User, Factory
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

FACTORIES = [
    {"name": "Coimbatore Plant A",   "type": "Textile Manufacturing",  "location": "Coimbatore, TN", "lat": 11.00, "lng": 76.96},
    {"name": "Chennai Thermal PP",   "type": "Thermal Power Plant",    "location": "Chennai, TN",    "lat": 13.08, "lng": 80.27},
    {"name": "Salem Steel Works",    "type": "Steel & Iron Industry",  "location": "Salem, TN",      "lat": 11.66, "lng": 78.14},
    {"name": "Tirupur Dyeing Unit",  "type": "Chemical Processing",    "location": "Tirupur, TN",    "lat": 11.10, "lng": 77.34},
    {"name": "Erode Cement Works",   "type": "Cement Production",      "location": "Erode, TN",      "lat": 11.34, "lng": 77.72},
    {"name": "Madurai Refinery",     "type": "Petroleum Refinery",     "location": "Madurai, TN",    "lat": 9.92,  "lng": 78.11},
]

with app.app_context():
    db.create_all()

    for f in FACTORIES:
        if not Factory.query.filter_by(name=f["name"]).first():
            db.session.add(Factory(**f))

    if not User.query.filter_by(username="admin").first():
        db.session.add(User(
            username="admin",
            email="admin@airguard.ai",
            password=bcrypt.generate_password_hash("admin123").decode("utf-8"),
            role="admin",
        ))

    db.session.commit()
    print("[AirGuard] Database initialized with sample factories and admin user.")
    print("           Username: admin  |  Password: admin123")
