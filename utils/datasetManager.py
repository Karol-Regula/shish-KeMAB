# here goes dataset conversions

import re
from textblob import TextBlob
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
        text = row['Text'].decode("utf8")
        c.execute('INSERT INTO tweets (content, value) VALUES (?, ?, ?);',
                  (text, row['Date'].decode("utf8"),
                   get_tweet_sentiment(text)))
        i += 1
        if (i % 1000 == 0):
            print i
    closeDB()
    return


def get_tweet_sentiment(text):
    # Could be refactored to be simpler, but screw it
    tweet = text
    indLink = tweet.find("http")
    if indLink != -1:
        if indLink == 0:
            return "none"
        else:
            tweet = tweet[0:indLink]  # Cut up to index of link
    indLink = tweet.find("pic.twitter.com")
    if indLink != -1:
        if indLink == 0:
            return "none"
        else:
            tweet = tweet[0:indLink]  # Cut up to index of link
    # print tweet.encode("utf-8")
    # Analyze using TextBlob
    analysis = TextBlob(sanitize_tweet(tweet))
    # print analysis.sentiment.polarity
    if analysis.sentiment.polarity > 0:
        return "pos"
    elif analysis.sentiment.polarity == 0:
        return "neut"
    else:
        return "neg"


def sanitize_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    Function credits to
    http://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


if __name__ == "__main__":
    # Use for testing
    parseTweets()


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
