from alchemy.config import db


class PeriodTimeDist(db.Model):
    __tablename__ = 'PeriodTimeDist'

    Partner_Id = db.Column('user_id', db.Integer, primary_key=True)
    Semester_Id = db.Column('proposal_id', db.Integer)
    Alloc0and1 = db.Column('proposal_id', db.Float)
    Alloc2 = db.Column('email', db.Float)
    Alloc3 = db.Column('email', db.Float)
    Used0and1 = db.Column('password', db.Float)
    Used2 = db.Column('role', db.Float)
    Used3 = db.Column('role', db.Float)


class Investigator(db.Model):
    __tablename__ = 'Investigator'

    Investigator_Id = db.Column('user_id', db.Integer, primary_key=True)
    Institute_Id = db.Column('proposal_id', db.Integer)
    FirstName = db.Column('proposal_id', db.Float)
    Surname = db.Column('email', db.Float)
    Email = db.Column('email', db.Float)
    Phone = db.Column('password', db.Float)
    PiptUser_Id = db.Column('role', db.Float)