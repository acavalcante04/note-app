from flask import Flask
from .config import Config
from .extensions import db
from .controllers.notebooks_controller import notebooks_bp
from .controllers.sections_controller import sections_bp
from .controllers.pages_controller import pages_bp

def create_app():
    # Define o caminho dos templates e arquivos estáticos apontando para o diretório frontend
    app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # Registro dos blueprints
    app.register_blueprint(notebooks_bp)
    app.register_blueprint(sections_bp)
    app.register_blueprint(pages_bp)
    
    return app
