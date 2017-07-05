from tac_api.alchemy.config import db


class Proposal(db.Model):
    __tablename__ = 'Proposals'

    Proposal_Id = db.Column('user_id', db.Integer, primary_key=True)
    proposalCode_Id = db.Column('proposal_id', db.Unicade)
    SchemaVersion = db.Column('proposal_id', db.Unicade)
    Current = db.Column('email', db.Unicode)
    Semester_Id = db.Column('email', db.Unicode)
    Title = db.Column('password', db.Unicode)
    Abstract = db.Column('role', db.Unicode)
    ReadMe = db.Column('role', db.Unicode)
    TotalReqTime = db.Column('role', db.Integer)
    ActOnAlert = db.Column('role', db.Integer)
    PriorityMod = db.Column('role', db.Integer)
    StatusComment = db.Column('role', db.Integer)
    Phase = db.Column('role', db.Integer)
    ProposalStatus_Id = db.Column('role', db.Integer)
    Submission = db.Column('role', db.Unicode)
    PhaseFinal = db.Column('role', db.Integer)
    SubmissionDate = db.Column('role', db.Unicode)
    ProposalInactiveReason_Id = db.Column('role', db.Unicode)
    OverheadTime = db.Column('role', db.Unicode)
    TimeUsed = db.Column('role', db.Unicode)
    ReleaseDate = db.Column('role', db.Unicode)
    TimeRestricted = db.Column('role', db.Unicode)
    P4 = db.Column('role', db.Unicode)
    Commissioning = db.Column('role', db.Unicode)
    ProposalType_Id = db.Column('role', db.Unicode)
    PRSummary = db.Column('role', db.Unicode)
    PRDisplay = db.Column('role', db.Unicode)
    NightlogSummary = db.Column('role', db.Unicode)


    def __repr__(self):
        return " email: {email}\t Role: {role} ".format(email=self.email, role=self.role)

    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role