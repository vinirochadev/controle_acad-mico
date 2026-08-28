# 🎓 Controle Acadêmico

> Aplicação web para gerenciamento acadêmico, desenvolvida com Python e Flask, permitindo administrar alunos, disciplinas e notas, além de gerar um relatório de desempenho por disciplina.

## 📌 Sobre o projeto

O **Controle Acadêmico** é uma aplicação web desenvolvida como Projeto Integrador de Desenvolvimento de Sistemas.

O sistema foi desenvolvido para centralizar informações acadêmicas e facilitar o gerenciamento de **alunos, disciplinas e notas** em uma única aplicação.

Além das operações de cadastro, edição e exclusão, o sistema possui filtros para consulta dos dados e um relatório que calcula a média das notas registradas para cada disciplina.

## ✨ Funcionalidades

### 👨‍🎓 Alunos

* Cadastro de alunos
* Edição de alunos
* Exclusão de alunos
* Consulta de alunos
* Filtro por curso
* Validação de nome, e-mail e curso

### 📚 Disciplinas

* Cadastro de disciplinas
* Edição de disciplinas
* Exclusão de disciplinas
* Consulta de disciplinas
* Filtro por professor
* Associação de disciplinas aos respectivos professores

### 📝 Notas

* Registro de notas
* Edição de notas
* Exclusão de notas
* Associação entre aluno e disciplina
* Validação de notas entre 0 e 10
* Filtros por aluno e disciplina

### 📊 Relatórios

* Cálculo da média das notas por disciplina
* Visualização das disciplinas e respectivas médias

## 🛠️ Tecnologias utilizadas

### Backend

* **Python 3**
* **Flask**
* **Flask-SQLAlchemy**
* **Flask-WTF**
* **WTForms**

### Banco de dados

* **SQLite**
* **SQLAlchemy ORM**

### Frontend

* **HTML5**
* **CSS**
* **Jinja2**

## 🗄️ Modelagem de dados

O sistema possui três entidades principais:

```text
┌──────────────┐
│    Aluno     │
├──────────────┤
│ id           │
│ nome         │
│ email        │
│ curso        │
└──────┬───────┘
       │
       │ 1:N
       ▼
┌──────────────┐
│     Nota     │
├──────────────┤
│ id           │
│ aluno_id     │
│ disciplina_id│
│ valor        │
└──────┬───────┘
       │
       │ N:1
       ▼
┌──────────────┐
│  Disciplina  │
├──────────────┤
│ id           │
│ nome         │
│ professor    │
└──────────────┘
```

Cada **Aluno** pode possuir diversas notas, enquanto cada **Disciplina** pode estar associada a diversas notas.

A entidade `Nota` funciona como elemento de relacionamento entre alunos e disciplinas, armazenando também o valor obtido.

## 🔄 Fluxo da aplicação

```text
                    ┌──────────────┐
                    │   Dashboard  │
                    └──────┬───────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      Alunos          Disciplinas         Notas
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                      Banco de Dados
                           │
                           ▼
                       Relatório
```

## 🧩 Validação de dados

O projeto utiliza **Flask-WTF e WTForms** para validação dos dados enviados pelos formulários.

Entre as validações implementadas estão:

* Campos obrigatórios
* Validação de e-mail
* Limitação de tamanho de campos
* Seleção válida de aluno e disciplina
* Notas dentro do intervalo de **0 a 10**

Essas regras são definidas nos formulários da aplicação.

## 📊 Relatório de desempenho

A aplicação possui uma rota específica para geração de relatório.

Para cada disciplina, o sistema recupera as notas associadas, calcula a média e apresenta os resultados na interface.

```text
Notas da disciplina
       │
       ▼
   Soma das notas
       │
       ▼
Quantidade de notas
       │
       ▼
     Média
```

## 📂 Estrutura do projeto

```text
PI_controleAcademico/
│
├── templates/
│
├── .gitignore
├── app.py
├── config.py
├── extensions.py
├── forms.py
├── init_db.py
├── models.py
├── requirements.txt
└── README.md
```

A aplicação utiliza uma estrutura modular simples, separando configuração, extensões, formulários e modelos da lógica principal da aplicação.

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/vinirochadev/PI_controleAcademico.git
cd PI_controleAcademico
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicialize o banco de dados

```bash
python init_db.py
```

### 5. Execute a aplicação

```bash
python app.py
```

### 6. Acesse no navegador

```text
http://127.0.0.1:5000
```

## 📚 Principais conceitos praticados

Este projeto permitiu aplicar conceitos importantes de desenvolvimento de sistemas, como:

* Desenvolvimento web com Flask
* Arquitetura baseada em rotas e templates
* ORM com SQLAlchemy
* Modelagem de entidades e relacionamentos
* Operações de CRUD
* Validação de formulários
* Relacionamentos entre tabelas
* Consultas e filtros no banco de dados
* Processamento de dados para geração de relatórios
* Organização e separação de responsabilidades no código

## 🎯 Objetivo acadêmico

O projeto foi desenvolvido como parte de um **Projeto Integrador de Desenvolvimento de Sistemas**, com o objetivo de aplicar conceitos de programação, banco de dados e desenvolvimento web na construção de um sistema acadêmico funcional.

## 👨‍💻 Autor

**Vinicius**

Desenvolvido como Projeto Integrador de Desenvolvimento de Sistemas.
