from flask import Flask, render_template , request , redirect
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


@app.route("/" , methods = ['GET','POST'])
def hello_world():
    if request.method == 'POST':
        title =  request.form['title']
        description = request.form['description']
        todo = Todo(Title=title , Description=description)
        db.session.add(todo)
        db.session.commit()
    all_todos = Todo.query.all()
    return render_template("index.html" , all_todos=all_todos)

@app.route("/update")
def update_data():
    # todo_item = Todo.query.filter_by(SNO = SNO).first()
    # db.session.delete(todo_item)
    # db.session.commit()
    return redirect("/")

@app.route("/delete/<int:SNO>")
def delete_data(SNO):
    todo_item = Todo.query.filter_by(SNO=SNO).first()
    db.session.delete(todo_item)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)