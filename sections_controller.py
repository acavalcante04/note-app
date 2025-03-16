from flask import Blueprint, render_template, request, redirect, url_for
from models import Section, Notebook
from extensions import db

sections_bp = Blueprint('sections_bp', __name__, template_folder='templates')

@sections_bp.route('/notebooks/<int:notebook_id>/sections')
def list_sections(notebook_id):
    notebook = Notebook.query.get_or_404(notebook_id)
    sections = notebook.sections
    return render_template('sections.html', notebook=notebook, sections=sections)

@sections_bp.route('/notebooks/<int:notebook_id>/sections/create', methods=['POST'])
def create_section(notebook_id):
    name = request.form.get('name')
    if name:
        new_section = Section(name=name, notebook_id=notebook_id)
        db.session.add(new_section)
        db.session.commit()
    return redirect(url_for('sections_bp.list_sections', notebook_id=notebook_id))
