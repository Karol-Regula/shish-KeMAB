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
    i = 0
    for row in tweets:
        c.execute('INSERT INTO tweets (content, value) VALUES (?, ?);', ((row['Text']).decode("utf8"), row['Date'].decode("utf8")))
        i += 1
        if (i % 1000 == 0):
            print i
    closeDB()
    return

def parseCrimes():
    initializeDB()
    i = 0
    crimes = csv.DictReader(open("../data/crimes.csv"))
    for row in crimes:
        d1 = row['CMPLNT_FR_DT'].decode("utf8")
        d2 = row['OFNS_DESC'].decode("utf8")
        d3 = row['LAW_CAT_CD'].decode("utf8")
        d4 = row['BORO_NM'].decode("utf8")
        if len(d1) > 8 and (d1[8] == str(1) or (d1[9] == str(9) and d1[8] == str(0))):
            c.execute('INSERT INTO crimes (value, type, level, borough) VALUES (?, ?, ?, ?);', (d1, d2, d3, d4))
            i += 1
            if (i % 1000 == 0):
                print i
    closeDB()
    return

def yearSort():
    initializeDB()
    q = 'SELECT value FROM tweets'
    date = c.execute(q)
    dates = date.fetchall()
    yearQuan = [[2009,0],[2010,0],[2011,0],[2012,0],[2013,0],[2014,0],[2015,0],[2016,0]]#there's an easier way, but idk...etc.
    for item in dates:
        yearS = item[0][:4]
        yearI = int(yearS)
        for i in range(len(yearQuan)):
            if yearQuan[i][0] == yearI:
                yearQuan[i][1] = yearQuan[i][1]+1
    closeDB()
    print yearQuan

def yearFind(year):
    initializeDB()
    tweets = []
    q = 'SELECT * FROM tweets'
    content = c.execute(q)
    allThings = content.fetchall()

    for item in allThings:
        yearS = item[1][:4]
        yearI = int(yearS)
        if (yearI == year):
            tweets.append(item[0])

    closeDB()
    print tweets

def monthSort():
    initializeDB()
    q = 'SELECT value FROM tweets'
    date = c.execute(q)
    dates = date.fetchall()
    monthQuan = [0,0,0,0,0,0,0,0,0,0,0,0,0]#there's an easier way, but idk -- jan is 1, feb is 2, etc. 0 is null
    for item in dates:
        monthS = item[0][5:7]
        monthI = int(monthS)
        monthQuan[monthI-1] = monthQuan[monthI-1]+1
    closeDB()
    print monthQuan

def monthFind(month):
    initializeDB()
    tweets = []
    q = 'SELECT * FROM tweets'
    content = c.execute(q)
    allThings = content.fetchall()

    for item in allThings:
        monthS = item[1][5:7]
        monthI = int(monthS)
        if (monthI == month):
            tweets.append(item[0])

    closeDB()
    print tweets

#crimes = csv.DictReader(open("data/crimes.csv"))#want: date, desc, category, boro
#parseTweets()
#monthSort()
#monthFind(12)
#yearSort()
#parseCrimes()
#yearFind(2011)
#levelSort()
