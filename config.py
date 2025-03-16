import os

class Config:
    SECRET_KEY = "alguma_senha_muito_secreta"
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # O arquivo do banco será criado dentro da pasta app
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'my_notes.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True