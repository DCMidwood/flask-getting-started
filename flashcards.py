from flask import Flask, render_template

from model import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
                "welcome.html",
                message="here is a message",
                x=23
    )


@app.route("/card")
def card_view():
    card = db[2]
    return render_template("card.html", card=card)


if __name__ == '__main__':
    app.run(debug=True)