from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello world 世界真美好"


if __name__ == '__main__':
    app.run(debug=True)
