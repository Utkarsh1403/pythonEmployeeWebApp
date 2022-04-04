from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():

    return "Welcome to my website hima"
@app.route("/contact")
def ContactPage():

    return "Contact page"

@app.route("/home")
def Home():

    return "Home page"

@app.route("/gallery")
def gallery():

    return "gallery"

if __name__ == "__main__":
    app.run(debug=True)