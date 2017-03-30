#here goes dataset conversions

import csv
import sqlite3


f = "database.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

tweets = csv.DictReader(open("../data/tweets.csv"))#want: text, date
#crimes = csv.DictReader(open("data/crimes.csv"))#want: date, desc, category, boro

#goodTweets = []
for row in tweets:
    #sql add row['Text'] to tweet table
    q = 'INSERT INTO tweets VALUES ("%s","%s")' % (row['Text'],row['Date'])

for row in 
#goodTweets['Text'] = tweets['Text']
#goodTweets[1] = tweets[1]

#print goodTweets
