from flask import Blueprint, render_template, request, redirect, url_for
from models import Notebook
from extensions import db

notebooks_bp = Blueprint('notebooks_bp', __name__, template_folder='templates')

@notebooks_bp.route('/notebooks')
def list_notebooks():
    notebooks = Notebook.query.all()
    return render_template('notebooks.html', notebooks=notebooks)

@notebooks_bp.route('/notebooks/create', methods=['POST'])
def create_notebook():
    name = request.form.get('name')
    if name:
        new_notebook = Notebook(name=name)
        db.session.add(new_notebook)
        db.session.commit()
    return redirect(url_for('notebooks_bp.list_notebooks'))
