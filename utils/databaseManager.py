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

def levelSort():
    initializeDB()
    out = [0, 0, 0]#felonies, violations, misdemeanors
    c.execute('SELECT count(*) FROM crimes WHERE (level = ?);', ("FELONY",))
    num = c.fetchall()
    out[0] = num[0][0]
    c.execute('SELECT count(*) FROM crimes WHERE (level = ?);', ("MISDEMEANOR",))
    num = c.fetchall()
    out[1] = num[0][0]
    c.execute('SELECT count(*) FROM crimes WHERE (level = ?);', ("VIOLATION",))
    num = c.fetchall()
    out[2] = num[0][0]
    closeDB()
    print out

levelSort()
