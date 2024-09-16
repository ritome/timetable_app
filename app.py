import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # 追加
from models import db, BusStop, BusSchedule


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bus_schedule.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Flask-Migrateの初期化
migrate = Migrate(app, db)


@app.route("/", methods=["GET", "POST"])
def index():
    bus_stops = BusStop.query.with_entities(BusStop.stop_name).distinct()
    selected_stop = None
    schedule = None
    if request.method == "POST":
        selected_stop = request.form.get("stop_name")
        if selected_stop:
            stop = BusStop.query.filter_by(stop_name=selected_stop).first()
            if stop:
                schedule = BusSchedule.query.filter_by(bus_stop_id=stop.id).all()
                
    return render_template("index.html", bus_stops=bus_stops, schedule=schedule, selected_stop=selected_stop)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
