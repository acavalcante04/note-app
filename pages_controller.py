from flask import Blueprint, render_template, request, redirect, url_for
from models import Page, Section
from extensions import db

pages_bp = Blueprint('pages_bp', __name__, template_folder='templates')

@pages_bp.route('/sections/<int:section_id>/pages')
def list_pages(section_id):
    section = Section.query.get_or_404(section_id)
    pages = section.pages
    return render_template('pages.html', section=section, pages=pages)

@pages_bp.route('/sections/<int:section_id>/pages/create', methods=['POST'])
def create_page(section_id):
    title = request.form.get('title')
    content = request.form.get('content')
    if title:
        new_page = Page(title=title, content=content, section_id=section_id)
        db.session.add(new_page)
        db.session.commit()
    return redirect(url_for('pages_bp.list_pages', section_id=section_id))
