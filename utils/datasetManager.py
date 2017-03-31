#here goes dataset conversions

import csv
import sqlite3
import initialize

f = "database.db"

def initializeDB():
    global c, db
    file = '../data/database.db'
    db = sqlite3.connect(file)
    c = db.cursor()
    initialize.createDB()
    return c

def closeDB():
    global db
    db.commit()
    db.close()

def parseTweets():
    initializeDB()
    tweets = csv.DictReader(open("../data/tweets.csv"))#want: text, date
    for row in tweets:
        c.execute('INSERT INTO tweets (content, value) VALUES (?, ?);', ((row['Text']).decode("utf8"), row['Date'].decode("utf8")))
        #print row['Date']
    closeDB()
    return

#crimes = csv.DictReader(open("data/crimes.csv"))#want: date, desc, category, boro
parseTweets()
