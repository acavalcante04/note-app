from flask import Flask
# Ajuste estes imports conforme sua estrutura:
# Se 'config.py' e 'extensions.py' estiverem na mesma pasta de 'app.py', use import local.
# Se estiverem em outro pacote, mude o caminho.
from .config import Config
from .extensions import db
# from .models import ...
# from .routes import main_bp  # Exemplo de blueprint

def create_app():
    """
    Função responsável por criar e configurar a instância Flask.
    Retorna a aplicação configurada.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)

    # Registre suas rotas ou blueprints aqui (exemplo comentado):
    # app.register_blueprint(main_bp)

    # Exemplo de rota simples:
    @app.route('/')
    def index():
        return "Olá, mundo! Aplicação Flask está rodando."

    return app
