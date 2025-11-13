from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from extensions import db
from forms import AlunoForm, DisciplinaForm, NotaForm
from models import Aluno, Disciplina, Nota
from sqlalchemy import func

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # ----------------------------
    # PÁGINA INICIAL
    # ----------------------------
    @app.route('/')
    def index():
        return render_template('index.html')

    # ----------------------------
    # CRUD DE ALUNOS
    # ----------------------------
    @app.route('/alunos', methods=['GET', 'POST'])
    def alunos():
        form = AlunoForm()
        if form.validate_on_submit():
            novo = Aluno(nome=form.nome.data, email=form.email.data, curso=form.curso.data)
            db.session.add(novo)
            db.session.commit()
            flash('Aluno cadastrado com sucesso!', 'success')
            return redirect(url_for('alunos'))
        alunos = Aluno.query.all()
        return render_template('alunos.html', form=form, alunos=alunos)

    @app.route('/alunos/editar/<int:id>', methods=['GET', 'POST'])
    def editar_aluno(id):
        aluno = Aluno.query.get_or_404(id)
        form = AlunoForm(obj=aluno)
        if form.validate_on_submit():
            aluno.nome = form.nome.data
            aluno.email = form.email.data
            aluno.curso = form.curso.data
            db.session.commit()
            flash('Dados do aluno atualizados!', 'info')
            return redirect(url_for('alunos'))
        return render_template('alunos.html', form=form, alunos=Aluno.query.all())

    @app.route('/alunos/excluir/<int:id>')
    def excluir_aluno(id):
        aluno = Aluno.query.get_or_404(id)
        db.session.delete(aluno)
        db.session.commit()
        flash('Aluno excluído com sucesso!', 'danger')
        return redirect(url_for('alunos'))

    # ----------------------------
    # CRUD DE DISCIPLINAS
    # ----------------------------
    @app.route('/disciplinas', methods=['GET', 'POST'])
    def disciplinas():
        form = DisciplinaForm()
        if form.validate_on_submit():
            nova = Disciplina(nome=form.nome.data, professor=form.professor.data)
            db.session.add(nova)
            db.session.commit()
            flash('Disciplina cadastrada com sucesso!', 'success')
            return redirect(url_for('disciplinas'))
        disciplinas = Disciplina.query.all()
        return render_template('disciplinas.html', form=form, disciplinas=disciplinas)

    @app.route('/disciplinas/editar/<int:id>', methods=['GET', 'POST'])
    def editar_disciplina(id):
        disciplina = Disciplina.query.get_or_404(id)
        form = DisciplinaForm(obj=disciplina)
        if form.validate_on_submit():
            disciplina.nome = form.nome.data
            disciplina.professor = form.professor.data
            db.session.commit()
            flash('Disciplina atualizada!', 'info')
            return redirect(url_for('disciplinas'))
        return render_template('disciplinas.html', form=form, disciplinas=Disciplina.query.all())

    @app.route('/disciplinas/excluir/<int:id>')
    def excluir_disciplina(id):
        disciplina = Disciplina.query.get_or_404(id)
        db.session.delete(disciplina)
        db.session.commit()
        flash('Disciplina excluída!', 'danger')
        return redirect(url_for('disciplinas'))

    # ----------------------------
    # CRUD DE NOTAS
    # ----------------------------
    @app.route('/notas', methods=['GET', 'POST'])
    def notas():
        form = NotaForm()
        form.aluno_id.choices = [(a.id, a.nome) for a in Aluno.query.all()]
        form.disciplina_id.choices = [(d.id, d.nome) for d in Disciplina.query.all()]

        if form.validate_on_submit():
            nova = Nota(aluno_id=form.aluno_id.data, disciplina_id=form.disciplina_id.data, valor=form.valor.data)
            db.session.add(nova)
            db.session.commit()
            flash('Nota registrada com sucesso!', 'success')
            return redirect(url_for('notas'))

        notas = Nota.query.all()
        return render_template('notas.html', form=form, notas=notas)

    # ----------------------------
    # RELATÓRIO
    # ----------------------------
    @app.route('/relatorio')
    def relatorio():
        dados = db.session.query(
            Aluno.nome.label('aluno'),
            Disciplina.nome.label('disciplina'),
            func.avg(Nota.valor).label('media')
        ).join(Nota, Nota.aluno_id == Aluno.id)\
         .join(Disciplina, Nota.disciplina_id == Disciplina.id)\
         .group_by(Aluno.id, Disciplina.id).all()

        return render_template('relatorio.html', relatorio=dados)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
