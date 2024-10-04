import sqlite3


def initiable_db():
    connection = sqlite3.connect('database_products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL   
    )    
    ''')
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_price ON Products (price)")
    connection.commit()
    connection.close()

    connection = sqlite3.connect(('database_users.db'))
    cursor = connection.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
            )    
            ''')
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('database_products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

    connection.commit()
    connection.close()

def add_user(username, email, age):
    connection = sqlite3.connect(('database_users.db'))
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f'{username}', f'{email}', f'{age}', 1000))

    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect(('database_users.db'))
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username, )).fetchone()
    if check_user is None:
        return False
    else:
        return True
    connection.commit()
    connection.close()



