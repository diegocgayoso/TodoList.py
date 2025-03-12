from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


# Modelo de tasks
class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(255), unique=True, nullable=False)
    completed = db.Column(db.Boolean, default=False)


# Rota principal
@app.route( "/" )
def home():
    # Read tasks
    tasks = Task.query.all()
    return render_template( "index.html", tasks=tasks )


# Rota de adicionar
@app.route("/add", methods=["POST"])
def add():
    description = request.form["description"]
    
    #Validação de tasks criadas
    existind_task = Task.query.filter_by(description=description).first()
    if existind_task:
        return "Erro: Tarefa já existe.", 400
    new_task = Task(description = description)
    db.session.add( new_task )
    db.session.commit()
    return redirect("/")

# Rota de deletar
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect("/")

# Rota de editar
@app.route("/edit/<int:task_id>", methods=["POST"])
def edit(task_id):
    task = Task.query.get(task_id)
    
    if task:
        task.description = request.form["description"]
        db.session.commit()
    return redirect("/")

# Rota de marcar como concluída
@app.route("/complete/<int:task_id>", methods=["POST"])
def completed(task_id):
    task = Task.query.get(task_id)
    
    if task.completed == False:
        task.completed = True
        db.session.commit()
    elif task.completed == True:
        task.completed = False
        db.session.commit()
    return redirect("/")

# inicializador
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)
