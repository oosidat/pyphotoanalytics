import datetime
from app import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    user_id = db.Column(db.String(), primary_key=True)
    is_finished = db.Column(db.Boolean, default=False)
    added_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return '<user_id {}'.format(self.id)
