from dotenv import load_dotenv
import os

load_dotenv()

class ApplicationConfig():
    JWT_SECRET_KEY=os.environ["JWT_SECRET_KEY"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///messaging_web_app.db"
    