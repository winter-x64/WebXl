from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/")
def help():
    return "hello, akhil"


if __name__ == "__main__":
    app.run()
