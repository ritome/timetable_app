from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# バス停のモデル
class BusStop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stop_name = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(5), nullable=False)  # 'time' カラムを追加


# 時刻表のモデル
# models.py
class BusSchedule(db.Model):
    __tablename__ = "bus_schedule"
    id = db.Column(db.Integer, primary_key=True)
    bus_stop_id = db.Column(db.Integer, db.ForeignKey("bus_stop.id"), nullable=False)
    departure_time = db.Column(db.String(5), nullable=False)
    destination = db.Column(db.String(100), nullable=True)  # destinationを省略可能に変更

    # バス停とのリレーション
    bus_stop = db.relationship("BusStop", backref=db.backref("schedules", lazy=True))
