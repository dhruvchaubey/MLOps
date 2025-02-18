from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return(" welcome home!")


@app.route("/index")
def index():
    return(" welcome to home!")

if __name__ == "__main__":
    app.run(debug = True)
    