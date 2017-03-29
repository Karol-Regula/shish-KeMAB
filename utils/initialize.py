#!/usr/bin/python
'''
block comment describing the contents of this file
'''
import sqlite3   #enable control of an sqlite database

f = "database.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#------------------------create tables---------------------------------------
q = "CREATE TABLE crimes (type TEXT, frequency INTEGER, time INTEGER)"
c.execute(q)

q = 'CREATE TABLE tweets (content TEXT, value INTEGER)'
c.execute(q)

db.commit()
db.close()
