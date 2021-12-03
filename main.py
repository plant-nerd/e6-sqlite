import csv
import sqlite3

def open_csv (file):
    fv = open(f"data/{file}", "r")
    dialect = csv.Sniffer().sniff(fv.read(10000))
    fv.seek(0)
    d = csv.DictReader(fv, dialect=dialect)
    return d

def print_csv (file):
    for line in open_csv(f'{file}'):
        print(line)

def create_tables ():
    with sqlite3.connect('data/cafe.sqlite3') as s3:
        s3.execute("""CREATE TABLE IF NOT EXISTS coffees (
       id INTEGER PRIMARY KEY,
       name  TEXT NOT NULL,
       type TEXT,
       cost_lb REAL
       	)
       """)
        s3.execute("""CREATE TABLE IF NOT EXISTS ratings (
               id INTEGER PRIMARY KEY,
               date  TEXT NOT NULL,
               store_name TEXT,
               rating INTEGER
               	)
               """)
        s3.execute("""CREATE TABLE IF NOT EXISTS specials (
               id INTEGER PRIMARY KEY,
               date  TEXT NOT NULL,
               store_name TEXT,
               coffee_name TEXT,
               price REAL
               	)
               """)
        s3.execute("""CREATE TABLE IF NOT EXISTS stores (
               id INTEGER PRIMARY KEY,
               name  TEXT NOT NULL,
               kind TEXT,
               volume INTEGER
               	)
               """)


if __name__ == "__main__":
    open_csv('coffees.csv')
    open_csv('ratings.csv')
    open_csv('specials.csv')
    open_csv('stores.csv')

create_tables()