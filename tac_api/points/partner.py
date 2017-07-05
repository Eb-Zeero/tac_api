from alchemy.config import db


class Partner(db.Model):
    __tablename__ = "partner"
    Partner_Id = db.Column(db.Integer, primary_key=True)
    Partner_Code = db.Column(db.String(10))
    Partner_Name = db.Column(db.String(100))
    TargetMod = db.Column(db.Integer)
    ProprietaryMax = db.Column(db.Interger)
    Virtual = db.Column(db.Interger)
