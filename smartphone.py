import sqlite3
from sys import path

class PrimaryKeyError(Exception):
    pass


data = sqlite3.connect(path[0]+"/smart_db.db",check_same_thread=False)
cur = data.cursor()

def craete_table():
    cur.execute("CREATE TABLE IF NOT EXISTS smart_table(code_id INTEGER PRIMARY KEY, price FLOAT, marke TEXT, year INTEGER, battery INTEGER)")


def insert_smart(code_id, price,marke,year,battery):
    try :
        cur.execute("INSERT INTO smart_table VALUES(?, ?, ?, ?, ?)",(code_id, price,marke,year,battery))
        data.commit()
    except(sqlite3.IntegrityError) :
        raise PrimaryKeyError("Code ID must be a unique number!")

def find_smart(codeid):
    cur.execute("SELECT * FROM smart_table WHERE code_id=?",[codeid])
    data.commit()

def update_smart(percent):
    cur.execute("UPDATE smart_table SET price=2*price WHERE code_id=?",[percent])
    data.commit()
    

def delete_smart(codeid):
    cur.execute("DELETE FROM smart_table WHERE code_id=?",[codeid])
    data.commit()

def allphone():
    return list(cur.execute("SELECT * FROM smart_table"))

