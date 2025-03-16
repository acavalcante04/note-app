from .extensions import db

class Notebook(db.Model):
    __tablename__ = 'notebooks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    # Relação 1:N com Section
    sections = db.relationship('Section', backref='notebook', lazy=True)

class Section(db.Model):
    __tablename__ = 'sections'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebooks.id'))
    # Relação 1:N com Page
    pages = db.relationship('Page', backref='section', lazy=True)

class Page(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=True)
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'))
