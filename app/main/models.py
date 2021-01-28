import arrow

from app import db
from sqlalchemy_utils import ArrowType


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False, info={'label': 'Name'})
    email = db.Column(db.Unicode(255), nullable=False, info={'label': 'E-mail'})


class Location(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=True, info={'label': 'Name'})
    event_id = db.Column(db.ForeignKey('event.id'))
    event = db.relationship('Event', backref=db.backref('locations',
                                                        cascade='all, delete-orphan'))


class Event(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    start_at = db.Column(db.Date(), nullable=False, info={'label': 'Start Date'})
    type = db.Column(db.String(), info={'choices': [('party', 'party'),
                                                    ('meeting', 'meeting')],
                                        'label': 'Activity Type',
                                        'description': 'Please specify the type of activity'})
    creator_id = db.Column(db.ForeignKey('user.id'))
    creator = db.relationship(User, backref=db.backref('events',
                                                       cascade='all, delete-orphan'))
