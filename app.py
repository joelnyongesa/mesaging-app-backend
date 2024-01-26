from flask import Flask
from flask_migrate import Migrate

from config import ApplicationConfig

from models import db, User, Agent, Message

app = Flask(__name__)

app.config.from_object(ApplicationConfig)

migrate = Migrate(app=app, db=db)

db.init_app(app=app)

if __name__ == "__main__":
    app.run(port=5555, debug=True)