from apps.app import db

class Itinerarys(db.Model):
    __tablename__ = "Itinerarys"
    id = db.Column(db.Integer, primary_key=True)
    itinerary = db.Column(db.String,index=True)
    date = db.Column(db.Date)
    start = db.Column(db.Time)
    end = db.Column(db.Time)