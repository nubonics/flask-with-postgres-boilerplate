from app import db


class Results(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    is_this_working = db.Column(db.Boolean(), default=True)

    def __init__(self, id, is_this_working):
        self.id = id
        self.is_this_working = is_this_working

    def __repr__(self):
        return '<id {}>'.format(self.id)
