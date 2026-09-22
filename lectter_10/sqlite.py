import sqlite3

conn = sqlite3.connect('my_database.db')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        city TEXT NOT NULL
    )
''')

cur.execute("INSERT INTO users (name, age, city) VALUES ('alice', 25, 'New York')")
cur.execute("INSERT INTO users (name, age, city) VALUES ('bob', 30, 'Los Angeles')")
cur.execute("INSERT INTO users (name, age, city) VALUES ('charlie', 35, 'Chicago')")

cur.execute('''
INSERT INTO users (name, age, city) VALUES
    ('Alice', 25, 'New York'),
    ('Bob', 30, 'Los Angeles'),
    ('Charlie', 35, 'Chicago')
''')


conn.commit()

cur.execute('SELECT * FROM users')
rows = cur.fetchall()

print("Users in the database:")
for row in rows:
    print(row)

conn.close()
