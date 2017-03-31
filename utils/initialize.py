#!/usr/bin/python
'''
block comment describing the contents of this file
'''
import sqlite3   #enable control of an sqlite database
def createDB():
  f = "../data/database.db"

  db = sqlite3.connect(f) #open if f exists, otherwise create
  c = db.cursor()    #facilitate db ops

  #------------------------create tables---------------------------------------
  q = "CREATE TABLE IF NOT EXISTS crimes (value TEXT, type TEXT, level TEXT, borough TEXT)"
  c.execute(q)

  q = 'CREATE TABLE IF NOT EXISTS tweets (content TEXT, value TEXT)'
  c.execute(q)

  db.commit()
  db.close()
