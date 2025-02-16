from flask import Flask, render_template
from  flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func  # Import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress a warning

db =  SQLAlchemy(app)

class Todo(db.Model):
    SNO          = db.Column(db.Integer, primary_key=True)
    Title        = db.Column(db.String(200), nullable=False)
    Description  = db.Column(db.String(500), nullable=False)  # Fixed data type
    Date_created = db.Column(db.DateTime, default=func.now())  # Fixed datetime reference


    def __repr__(self):
        return f"{self.SNO} {self.Title}"


@app.route("/")
def hello_world():
    todo = Todo(Title="First Todo" , Description="Start Investing in BTC")
    db.session.add(todo)
    db.session.commit()
    all_todos = Todo.query.all()
    return render_template("index.html" , all_todos=all_todos)

@app.route("/show")
def products():
    all_todo = Todo.query.all()
    return "<p>This is Porduct Page! </p>"


if __name__ == "__main__":
    app.run(debug=True)