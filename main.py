from flask import Flask
from styles import make_bold, make_italic, make_underlined

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align:center;">Hello World</h1>' \
        '<p>This is a paragraph</p>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'    \
        '<div style="width:300px"><iframe allow="fullscreen" frameBorder="0" height="300" src="https://giphy.com/embed/LztiZcUGIdOxwan65U/video" width="480"></iframe></div>'

@app.route("/bye")
@make_bold
@make_italic
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)
