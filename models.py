from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from uuid import uuid4
from faker import Faker

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex

class User(db.Model, SerializerMixin):

    __tablename__ = "users"

    serialize_rules=("-messages.user")

    id = db.Column(db.String, primary_key=True, unique=True, default=get_uuid)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone_number = db.Column(db.String(10))
    email_address = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_defalt=db.func.now())

    messages = db.relationship('Message', backref='user')

    def __repr__(self):
        return f"User id: {self.id}\nName: {self.first_name} {self.last_name}"


class Agent(db.Model, SerializerMixin):

    __tablename__ = "agents"

    serialize_rules=("-messages.agent")

    id = db.Column(db.String, primary_key=True, unique=True, default=get_uuid)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    category = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_defalt=db.func.now())

    messages = db.relationship('Message',backref='agent')

    def __repr__(self):
        return f"Agent id: {self.id}\nName: {self.first_name} {self.last_name}"


class Message(db.Model, SerializerMixin):

    __tablename__ = "messages"

    serialize_rules = ("-user.messages", "-agent.messages")

    id = db.Column(db.String, primary_key=True, unique=True, default=get_uuid)
    category = db.Column(db.String)
    body = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    user_id = db.Column(db.String, db.ForeignKey("users.id"))
    agent_id = db.Column(db.String, db.ForeignKey("agents.id"))

    def __repr__(self):
        return f"Message: {self.id}\nCategory: {self.category}\nBody: {self.body}"