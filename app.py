from flask import Flask, render_template, request, redirect, url_for
import utils
from utils import datasetManager, databaseManager, initialize

app = Flask(__name__)


@app.route("/")
def placeholder0():
    return


@app.route("/data")
def data():
    out = databaseManager.sentQuan()
    print out
    return render_template('test.html', test=out)


@app.route("/build")
def placeholder1():
    return


@app.route("/graph")
def placeholder2():
    return


if __name__ == "__main__":
    app.debug = True
    # app.config.from_object("config")
    # app.secret_key = app.config["SECRET_KEY"]
    app.run()
