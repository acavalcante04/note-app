# Exemplo se a função create_app estiver em backend/app.py
from backend.app import create_app
from backend.extensions import db

app = create_app()

with app.app_context():
    db.create_all()
    print("Banco de dados criado!")
