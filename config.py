from dotenv import load_dotenv
import os

load_dotenv()

class ApplicationConfig():
    SECRET_KEY =os.environ["SECRET_KEY"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///messaging_web_app.db"
    JSONIFY_PRETTYPRINT_REGULAR = False