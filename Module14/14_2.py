import sqlite3

connetion = sqlite3.connect('not_telegram2.db')
cursor = connetion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f'user{i}', f'example{i}@gmail.com', f'{i*10}', 1000))

for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id=?", (i, ))

cursor.execute("SELECT * FROM Users WHERE age != 60")
for user in cursor.fetchall():
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

cursor.execute("DELETE FROM users WHERE id = ?", (6,))

cursor.execute("SELECT COUNT(*) FROM Users")
count_user = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]

print(total_balance/count_user)


connetion.commit()
connetion.close()