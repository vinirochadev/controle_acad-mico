from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from extensions import db
from forms import AlunoForm
from models import Aluno

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # ----------------------------
    # ROTA PRINCIPAL
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

    return app


# 🔹 ESTE BLOCO É ESSENCIAL 🔹
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
