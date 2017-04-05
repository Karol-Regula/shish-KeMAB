from flask import Flask, render_template, request, redirect, url_for
import utils
from utils import datasetManager, databaseManager, initialize

app = Flask(__name__)


@app.route("/")
def placeholder0():
    return redirect(url_for('data'))


@app.route("/data")
def data():
    out0 = databaseManager.getCrimesInDateAll0()
    out1 = databaseManager.getCrimesInDateAll1()
    tweets = databaseManager.datesQuan()
    sent = databaseManager.sentQuan()
    sample = databaseManager.totalContent()
    #print sample
    return render_template('test.html', test = out0, test2 = out1, tweets = tweets, sent = sent, sample = sample)


@app.route("/build")
def build():
    #datasetManager.parseTweets()
    #databaseManager.findCrimesInDateAll()
    databaseManager.getCrimesInDateAll()
    return


@app.route("/graph")
def placeholder2():
    return


if __name__ == "__main__":
    app.debug = True
    # app.config.from_object("config")
    # app.secret_key = app.config["SECRET_KEY"]
    app.run()
