import csv
import sqlite3
import cafe_data

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

def drop_tables():
   with sqlite3.connect('data/cafe.sqlite3') as s3:
       s3.execute("DROP TABLE if exists coffees")
       s3.execute("DROP TABLE if exists specials")
       s3.execute("DROP TABLE if exists ratings")
       s3.execute("DROP TABLE if exists stores")


if __name__ == "__main__":
    cafe_data.open_csv('coffees.csv')
    cafe_data.open_csv('ratings.csv')
    cafe_data.open_csv('specials.csv')
    cafe_data.open_csv('stores.csv')

create_tables()

cafe_data.load_cafe_data()