from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired, Email, Length, NumberRange

# ---------------------
# Formulário de Aluno
# ---------------------
class AlunoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    curso = StringField('Curso', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Salvar')

# ---------------------
# Formulário de Disciplina
# ---------------------
class DisciplinaForm(FlaskForm):
    nome = StringField('Nome da Disciplina', validators=[DataRequired(), Length(min=2, max=100)])
    professor = StringField('Professor', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Salvar')

# ---------------------
# Formulário de Nota
# ---------------------
class NotaForm(FlaskForm):
    aluno_id = SelectField('Aluno', coerce=int, validators=[DataRequired()])
    disciplina_id = SelectField('Disciplina', coerce=int, validators=[DataRequired()])
    valor = FloatField('Nota', validators=[DataRequired(), NumberRange(min=0, max=10)])
    submit = SubmitField('Salvar')
