from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Simple function """
    return "Hello World"


@app.route("/about")
def about():
    """Simple function """
    return "Página sobre"

if __name__ == "__main__":
    app.run(debug=True)
