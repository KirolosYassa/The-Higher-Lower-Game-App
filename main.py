from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align:center;'>Hello World</h1>" \
        "<p>This is a paragraph</p>" \
                "<img src='https://giphy.com/gifs/bestfriends-save-them-all-best-friends-animal-society-bfas-tHwPSFm0WO8KXLcxkz' width='300px' height='300px' />"


if __name__ == "__main__":
    app.run(debug=True)
