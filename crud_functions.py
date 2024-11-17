import sqlite3

connect = sqlite3.connect("database.db")
curs = connect.cursor()


def initiate_db():
    curs.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price TEXT
    )
    ''')
    curs.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    connect.commit()


products_data = [
    ('1', 'Product 1', 'Солгар натуральный растительный комплекс', '2139р'),
    ('2', 'Product 2', 'Солгар комплекс мультивитаминов', '2596р'),
    ('3', 'Product 3', 'Солгар витамин C 500 mg', '1145р'),
    ('4', 'Product 4', 'Солгар MULTI-ONE', '1888р')
]
initiate_db()
# curs.executemany('INSERT INTO Products VALUES(?,?,?,?)', products_data)


def add_user(username, email, age, balance=1000):
    curs.execute('INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,?)',
                 (username, email, age, balance))
    connect.commit()


def is_included(username):
    curs.execute("SELECT * FROM Users")
    user_list = curs.fetchall()

    for user in user_list:
        if username == user[1]:
            return True
        else:
            return False


def get_all_products():
    curs.execute("SELECT * FROM Products")
    return curs.fetchall()
