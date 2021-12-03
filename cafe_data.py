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

def load_cafe_data ():
    #soooo you gotta go through the files
    #line by line
    coffees = open_csv('coffees.csv')
    with sqlite3.connect('data/cafe.sqlite3') as s3:
        for line in coffees:
            s3.execute('INSERT INTO coffees (name,type,cost_lb)VALUES (:name, :type, :cost_lb)', line)
    ratings = open_csv('ratings.csv')
    with sqlite3.connect('data/cafe.sqlite3') as s3:
        for line in ratings:
            s3.execute('INSERT INTO ratings (date,store_name,rating)VALUES (:date, :store_name, :rating)', line)
    specials = open_csv('specials.csv')
    with sqlite3.connect('data/cafe.sqlite3') as s3:
        for line in specials:
            s3.execute('INSERT INTO specials (date,store_name,coffee_name,price)VALUES (:date, :store_name, :coffee_name, :price)', line)
    stores = open_csv('stores.csv')
    with sqlite3.connect('data/cafe.sqlite3') as s3:
        for line in stores:
            s3.execute('INSERT INTO stores (name,kind,volume)VALUES (:name, :kind, :volume)', line)


    '''for doc in data_folder:
        for line in doc:
            add(line) to table(same name)
    for line in (data/coffees.csv)
        data/cafe.sqlite3.coffees.append(line)'''