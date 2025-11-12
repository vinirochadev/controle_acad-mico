from flask import Flask, render_template
from extensions import db


def create_app():
    # cria a aplicação
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    from models import Aluno

    # rota principal
    @app.route('/')
    def index():
        alunos = Aluno.query.all()
        return render_template('index.html', alunos=alunos)
    return app


# executa o servidor local
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
