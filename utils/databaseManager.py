import csv
import sqlite3
import initialize

f = "database.db"


def initializeDB():
    global c, db
    file = 'data/database.db'
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
    out = [0, 0, 0]  # felonies, violations, misdemeanors
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


# returns amount of crimes in a specific month and year
def findCrimesInDate(month, year):
    initializeDB()
    out = 0
    c.execute('SELECT value FROM crimes;')
    dates = c.fetchall()
    for date in dates:
        date = date[0]
        if date[8:] == year:
            if date[0:2] == month:
                out += 1
    closeDB()
    print 'month: ' + month + ', year: ' + year
    print 'amount: ' + str(out)
    return out


def findCrimesInDateAll():  # runs the findCrimesIn function for each month and year, returns array
    out = []
    months = ['01', '02', '03', '04', '05',
              '06', '07', '08', '09', '10', '11', '12']
    years = ['09', '10', '11', '12', '13', '14', '15', '16']
    for y in years:
        for m in months:
            out.append(findCrimesInDate(m, y))
    initializeDB()
    c.execute(
        'INSERT INTO parsed (content, array) VALUES ("findCrimesInDateAll", ?);', (str(out),))
    closeDB()
    print out
    return out


def getCrimesInDateAll():  # retreives ready data from parsed table
    initializeDB()
    c.execute('SELECT array FROM parsed WHERE (content = "findCrimesInDateAll");')
    out = c.fetchall()
    closeDB()
    print out[0][0]
    return out[0][0]


def yearSort():
    initializeDB()
    q = 'SELECT value FROM tweets'
    date = c.execute(q)
    dates = date.fetchall()
    yearQuan = [[2009, 0], [2010, 0], [2011, 0], [2012, 0], [2013, 0], [
        2014, 0], [2015, 0], [2016, 0]]  # there's an easier way, but idk...
    for item in dates:
        yearS = item[0][:4]
        yearI = int(yearS)
        for i in range(len(yearQuan)):
            if yearQuan[i][0] == yearI:
                yearQuan[i][1] = yearQuan[i][1] + 1
    closeDB()
    print yearQuan
    return yearQuan


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
    return tweets


def monthSort():
    initializeDB()
    q = 'SELECT value FROM tweets'
    date = c.execute(q)
    dates = date.fetchall()
    monthQuan = [0] * 12  # thanks misha!
    for item in dates:
        monthS = item[0][5:7]
        monthI = int(monthS)
        monthQuan[monthI - 1] = monthQuan[monthI - 1] + 1
    closeDB()
    print monthQuan
    return monthQuan


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
    return tweets

# array of quantity of tweets from each month: [jan 2009, feb 2009, ..., dec 2016]
def datesQuan():
    initializeDB()
    q = 'SELECT value FROM tweets'
    date = c.execute(q)
    dates = date.fetchall()
    datesQuan = [0] * 12 * 8  # thanks Misha!
    for item in dates:
        monthS = item[0][5:7]
        monthI = int(monthS)
        yearS = item[0][:4]
        yearI = int(yearS)
        start = yearI - 2009
        end = start * 12 + monthI - 1
        datesQuan[end] += 1
    closeDB()
    print datesQuan
    return datesQuan

def sentQuan():
    initializeDB()
    q = 'SELECT * FROM tweets'
    tweet = c.execute(q)
    tweets = tweet.fetchall()
    sentQuan = [0] * 12 * 8  # thanks Misha!
    for item in tweets:
        monthS = item[1][5:7]
        monthI = int(monthS)
        yearS = item[1][:4]
        yearI = int(yearS)
        start = yearI - 2009
        end = start * 12 + monthI - 1
        print item[2]
        if (item[2] != -2):
            sentQuan[end] += item[2]
    closeDB()
    #print sentQuan
    return sentQuan


def datesContent(month, year):
    initializeDB()
    tweets = []
    q = 'SELECT * FROM tweets'
    content = c.execute(q)
    allThings = content.fetchall()

    for item in allThings:
        monthS = item[1][5:7]
        monthI = int(monthS)
        yearS = item[1][:4]
        yearI = int(yearS)
        if (monthI == month and yearI == year):
            tweets.append(item[0])

    closeDB()
    print tweets[0]
    return tweets


# monthSort()
# monthFind(12)
# yearSort()
# yearFind(2011)
# levelSort()
# findCrimesInDate('03', '14')#(March, 2014)
# findCrimesInDate('05', '11')
# findCrimesInDateAll()
getCrimesInDateAll()
# datesContent(2,2011)
