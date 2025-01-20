import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    INVITE_CODE = os.getenv("INVITE_CODE", "123")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    USE_SQLITE = os.getenv("USE_SQLITE", "True").lower() == "true"

    if USE_SQLITE:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.path.abspath(os.path.dirname(__file__)), "db.sqlite3")}"
    else:
        DB_ENGINE = os.getenv("DB_ENGINE")
        DB_USERNAME = os.getenv("DB_USERNAME")
        DB_PASS = os.getenv("DB_PASS")
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        DB_NAME = os.getenv("DB_NAME")

        SQLALCHEMY_DATABASE_URI = f"{DB_ENGINE}://{DB_USERNAME}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
