from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from extensions import db
from forms import AlunoForm, DisciplinaForm, NotaForm
from models import Aluno, Disciplina, Nota


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # ----------------------------
    # PÁGINA INICIAL
    # ----------------------------
    @app.route('/')
    def index():
        total_alunos = Aluno.query.count()
        total_disciplinas = Disciplina.query.count()
        total_notas = Nota.query.count()

        return render_template(
            'index.html',
            total_alunos=total_alunos,
            total_disciplinas=total_disciplinas,
            total_notas=total_notas
        )

    # ----------------------------
    # CRUD DE ALUNOS
    # ----------------------------
    @app.route('/alunos', methods=['GET', 'POST'])
    def alunos():
        form = AlunoForm()

        curso_filtro = request.args.get("curso", "", type=str)

        # Query base
        query = Aluno.query

        if curso_filtro:
            query = query.filter(Aluno.curso == curso_filtro)

        alunos = query.all()

        # Cadastro normal
        if form.validate_on_submit():
            novo = Aluno(
                nome=form.nome.data,
                email=form.email.data,
                curso=form.curso.data
            )
            db.session.add(novo)
            db.session.commit()
            flash("Aluno cadastrado!", "success")
            return redirect(url_for("alunos"))

        cursos = [c[0] for c in db.session.query(Aluno.curso).distinct().all()]

        return render_template(
            "alunos.html",
            form=form,
            alunos=alunos,
            cursos=cursos,
            curso_filtro=curso_filtro
        )

    @app.route('/alunos/editar/<int:id>', methods=['GET', 'POST'])
    def editar_aluno(id):
        aluno = Aluno.query.get_or_404(id)
        form = AlunoForm(obj=aluno)

        if form.validate_on_submit():
            form.populate_obj(aluno)
            db.session.commit()
            flash('Aluno atualizado com sucesso!', 'success')
            return redirect(url_for('alunos'))

        return render_template('partials/editar_aluno.html', form=form, aluno=aluno)

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

        professor_filtro = request.args.get("professor", "", type=str)

        query = Disciplina.query

        if professor_filtro:
            query = query.filter(Disciplina.professor == professor_filtro)

        disciplinas = query.all()

        if form.validate_on_submit():
            nova = Disciplina(
                nome=form.nome.data,
                professor=form.professor.data
            )
            db.session.add(nova)
            db.session.commit()
            flash("Disciplina cadastrada!", "success")
            return redirect(url_for("disciplinas"))

        professores = [p[0] for p in db.session.query(Disciplina.professor).distinct().all()]

        return render_template(
            "disciplinas.html",
            form=form,
            disciplinas=disciplinas,
            professores=professores,
            professor_filtro=professor_filtro
        )

    @app.route('/disciplinas/editar/<int:id>', methods=['GET', 'POST'])
    def editar_disciplina(id):
        disciplina = Disciplina.query.get_or_404(id)
        form = DisciplinaForm(obj=disciplina)

        if form.validate_on_submit():
            form.populate_obj(disciplina)
            db.session.commit()
            flash('Disciplina atualizada com sucesso!', 'success')
            return redirect(url_for('disciplinas'))

        return render_template('partials/editar_disciplina.html', form=form, disciplina=disciplina)

    @app.route('/disciplinas/excluir/<int:id>')
    def excluir_disciplina(id):
        disciplina = Disciplina.query.get_or_404(id)

        if disciplina.notas:
            flash('Não é possível excluir: Existem notas vinculadas.', 'danger')
            return redirect(url_for('disciplinas'))

        db.session.delete(disciplina)
        db.session.commit()
        flash('Disciplina excluída com sucesso!', 'success')
        return redirect(url_for('disciplinas'))

    # ----------------------------
    # CRUD DE NOTAS
    # ----------------------------
    @app.route('/notas', methods=['GET', 'POST'])
    def notas():
        form = NotaForm()

        form.aluno_id.choices = [(a.id, a.nome) for a in Aluno.query.all()]
        form.disciplina_id.choices = [(d.id, d.nome) for d in Disciplina.query.all()]

        aluno_filtro = request.args.get("aluno", "", type=str)
        disciplina_filtro = request.args.get("disciplina", "", type=str)

        query = Nota.query.join(Aluno).join(Disciplina)

        if aluno_filtro:
            query = query.filter(Aluno.id == int(aluno_filtro))

        if disciplina_filtro:
            query = query.filter(Disciplina.id == int(disciplina_filtro))

        notas = query.all()

        if form.validate_on_submit():
            nova = Nota(
                aluno_id=form.aluno_id.data,
                disciplina_id=form.disciplina_id.data,
                valor=form.valor.data
            )
            db.session.add(nova)
            db.session.commit()
            flash("Nota registrada!", "success")
            return redirect(url_for("notas"))

        alunos_select = Aluno.query.all()
        disciplinas_select = Disciplina.query.all()

        return render_template(
            "notas.html",
            form=form,
            notas=notas,
            alunos_select=alunos_select,
            disciplinas_select=disciplinas_select,
            aluno_filtro=aluno_filtro,
            disciplina_filtro=disciplina_filtro
        )

    @app.route('/notas/editar/<int:id>', methods=['GET', 'POST'])
    def editar_nota(id):
        nota = Nota.query.get_or_404(id)
        form = NotaForm(obj=nota)

        form.aluno_id.choices = [(a.id, a.nome) for a in Aluno.query.all()]
        form.disciplina_id.choices = [(d.id, d.nome) for d in Disciplina.query.all()]

        if form.validate_on_submit():
            form.populate_obj(nota)
            db.session.commit()
            flash('Nota atualizada com sucesso!', 'success')
            return redirect(url_for('notas'))

        return render_template('partials/editar_nota.html', form=form, nota=nota)

    @app.route('/notas/excluir/<int:id>')
    def excluir_nota(id):
        nota = Nota.query.get_or_404(id)
        db.session.delete(nota)
        db.session.commit()
        flash('Nota excluída com sucesso!', 'success')
        return redirect(url_for('notas'))

    # ----------------------------
    # RELATÓRIO
    # ----------------------------
    @app.route('/relatorio')
    def relatorio():
        disciplinas = Disciplina.query.all()

        labels = []
        medias = []

        for d in disciplinas:
            notas = [n.valor for n in d.notas]
            media = sum(notas) / len(notas) if notas else 0
            labels.append(d.nome)
            medias.append(round(media, 2))

        return render_template(
            'relatorio.html',
            labels=labels,
            medias=medias
        )

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
