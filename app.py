from flask import Flask, render_template
from  flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func  # Import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress a warning

db =  SQLAlchemy(app)

class Todo(db.Model):
    sno          = db.Column(db.Integer, primary_key=True)
    title        = db.Column(db.String(200), nullable=False)
    description  = db.Column(db.String(500), nullable=False)  # Fixed data type
    date_created = db.Column(db.DateTime, default=func.now())  # Fixed datetime reference



@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/products")
def products():
    return "<p>This is Porduct Page! </p>"


if __name__ == "__main__":
    app.run(debug=True)