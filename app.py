from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/product")
def products():
    return "<p>This is Porduct Page!</p>"


if __name__ == "__main__":
    app.run(debug=True)