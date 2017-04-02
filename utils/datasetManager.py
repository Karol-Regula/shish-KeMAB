# here goes dataset conversions

import csv
import sqlite3
import initialize

f = "database.db"


def initializeDB():
    global c, db
    file = '/data/database.db'
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
    tweets = csv.DictReader(open("/data/tweets.csv"))  # want: text, date
    i = 0
    for row in tweets:
        c.execute('INSERT INTO tweets (content, value) VALUES (?, ?);',
                  ((row['Text']).decode("utf8"), row['Date'].decode("utf8")))
        i += 1
        if (i % 1000 == 0):
            print i
    closeDB()
    return


def parseCrimes():
    initializeDB()
    i = 0
    crimes = csv.DictReader(open("/data/crimes.csv"))
    for row in crimes:
        d1 = row['CMPLNT_FR_DT'].decode("utf8")
        d2 = row['OFNS_DESC'].decode("utf8")
        d3 = row['LAW_CAT_CD'].decode("utf8")
        d4 = row['BORO_NM'].decode("utf8")
        if len(d1) > 8 and (d1[8] == str(1) or (d1[9] == str(9) and d1[8] == str(0))):
            c.execute(
                'INSERT INTO crimes (value, type, level, borough) VALUES (?, ?, ?, ?);', (d1, d2, d3, d4))
            i += 1
            if (i % 1000 == 0):
                print i
    closeDB()
    return

# parseCrimes()
# parseTweets()
