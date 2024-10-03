import sqlite3

connection = sqlite3.connect('database_products.db')
cursor = connection.cursor()

def initiable_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL   
    )    
    ''')

def get_all_products():
    connection = sqlite3.connect('database_products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

    connection.commit()
    connection.close()

cursor.execute("CREATE INDEX IF NOT EXISTS idx_price ON Products (price)")

# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Products {i}', f'Описание {i}', i*100))
get_all_products()

connection.commit()
connection.close()

