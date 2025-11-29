from extensions import db

# ---------------------
# Modelo de Aluno
# ---------------------
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    curso = db.Column(db.String(100), nullable=False)

    notas = db.relationship('Nota', backref='aluno', lazy=True)

    def __repr__(self):
        return f"<Aluno {self.nome}>"


# ---------------------
# Modelo de Disciplina
# ---------------------
class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    professor = db.Column(db.String(120), nullable=False)

    notas = db.relationship('Nota', backref='disciplina', lazy=True)

    def __repr__(self):
        return f"<Disciplina {self.nome}>"


# ---------------------
# Modelo de Nota
# ---------------------
class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'), nullable=False)
    valor = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Nota Aluno:{self.aluno_id} Disciplina:{self.disciplina_id} Valor:{self.valor}>"
