from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# cria a aplicação
app = Flask(__name__)
app.config.from_object('config.Config')

# inicializa o banco (vamos usar depois)
db = SQLAlchemy(app)


# rota principal
@app.route('/')
def index():
    return render_template('index.html')


# executa o servidor local
if __name__ == '__main__':
    app.run(debug=True)
